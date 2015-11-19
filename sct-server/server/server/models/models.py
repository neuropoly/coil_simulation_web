import datetime
import os
import simplejson as json
from uuid import uuid4

from sqlalchemy import Column, Integer, UnicodeText, Unicode, DateTime, ForeignKey, Float, LargeBinary, Boolean
from sqlalchemy.ext.declarative import declared_attr, declarative_base
from sqlalchemy.ext.mutable import Mutable
from sqlalchemy.orm import relationship, backref, synonym
from sqlalchemy.types import TypeDecorator, VARCHAR
from cryptacular import bcrypt

try:
    from server import cfg
except ImportError:
    import cfg


###################################################################################
# Custom column type to save python mutable
class JSONEncodedDict(TypeDecorator):
    "Represents an immutable structure as a json-encoded string."

    impl = VARCHAR

    def process_bind_param(self, value, dialect):
        if value is not None:
            value = json.dumps(value)
        return value

    def process_result_value(self, value, dialect):
        if value is not None:
            value = json.loads(value)
        return value


class MutableDict(Mutable, dict):
    @classmethod
    def coerce(cls, key, value):
        "Convert plain dictionaries to MutableDict."

        if not isinstance(value, MutableDict):
            if isinstance(value, dict):
                return MutableDict(value)

            # this call will raise ValueError
            return Mutable.coerce(key, value)
        else:
            return value

    def __setitem__(self, key, value):
        "Detect dictionary set events and emit change events."

        dict.__setitem__(self, key, value)
        self.changed()

    def __delitem__(self, key):
        "Detect dictionary del events and emit change events."

        dict.__delitem__(self, key)
        self.changed()


###################################################################################
# Base model for Table
class ModelBase(object):
    id = Column(Integer,autoincrement=True, primary_key=True)
    created_on = Column(DateTime, default=datetime.datetime.now)
    updated_on = Column(DateTime, onupdate=datetime.datetime.now)

    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower()


Base = declarative_base(cls=ModelBase)
crypt = bcrypt.BCRYPTPasswordManager()

###################################################################################
# Tables
class User(Base):
    email = Column(Unicode(1024), unique=True)
    first_name = Column(Unicode(1024))
    last_name = Column(Unicode(1024))
    password_ = Column('password', Unicode(60)) # Hash from bcrypt
    @property
    def password(self):
        return self.password_
    @password.setter
    def password(self, password):
        self.password_ = str(crypt.encode(password))
    password = synonym('password_', descriptor=password)

    @classmethod
    def by_mail(cls, email, session):
        return session.query(User).filter(User.email == email).first()
    def verify_password(self, password):
        'Return True if we have a matching password'
        return crypt.check(self.password, password)
    def serialize(self):
        return {
            '_id': self.id,
            'email': self.email,
            'first_name': self.first_name,
            'last_name': self.last_name
            # other fields that you need in the json
        }
    def __repr__(self):
        return "User%i(fullname='%s %s', email='%s')" \
               % (self.id,self.first_name, self.last_name, self.email)


class local_user(Base):
    email = Column(Unicode(1024), unique=True)
    country = Column(Unicode(1024), unique=False)
    research_center = Column(Unicode(1024), unique=False)
    occupation = Column(Unicode(1024), unique=False)
    password_ = Column('password', Unicode(60)) # Hash from bcrypt
    confirmed = Column(Boolean, unique=False, default=False)
    confirmed_on = Column(DateTime, unique=False)
    @property
    def password(self):
        return self.password_
    @password.setter
    def password(self, password):
        self.password_ = str(crypt.encode(password))
    password = synonym('password_', descriptor=password)
    @classmethod
    def by_mail(cls, email, session):
        return session.query(local_user).filter(local_user.email == email).first()
    def verify_password(self, password):
        'Return True if we have a matching password'
        return crypt.check(self.password, password)

class File(Base):
    filename = Column(Unicode(1024), unique=False)
    serverpath = Column(Unicode(1024), unique=False)
    localpath = Column(Unicode(1024), unique=False)
    type = Column(Unicode(1024), unique=False)
    size = Column(Float, unique=False)
    text = Column(Unicode(1024), unique=False)
    type = Column(Unicode(1024), unique=False)
    children = Column(Unicode(1024), unique=False)
    icon = Column(Unicode(1024), unique=False)
    user_id = Column(Unicode(1024), ForeignKey('user.id'))
    user = relationship("User", backref='files', order_by='User.id')

    def __repr__(self):
        return "<File(filename='%s', type='%s', localpath='%s')>" \
               % (self.filename, self.type, self.localpath)

class tree(Base):
    rel_path = Column(Unicode(1024), unique=False)
    parent = Column(Unicode(1024), unique=False)
    id = Column(Unicode(1024), unique=False, primary_key=True)
    size = Column(Float, unique=False)
    text = Column(Unicode(1024), unique=False)
    type = Column(Unicode(1024), unique=False)
    icon = Column(Unicode(1024), unique=False)
    state = Column(Unicode(1024), unique=False)
    deleted = Column(Boolean, unique=False, default=False)


class Operation(Base):
    args = Column(Unicode(1024), unique=False)
    input_path = Column(Unicode(1024), unique=True)
    output_path = Column(Unicode(1024), unique=True)
    name = Column(Unicode(1024), ForeignKey("registeredtool.name"))
    file_id = Column(Unicode(1024), ForeignKey("file.id"))
    
class Command(Base):
    expire_on = Column(DateTime, nullable=False)
    command_id = Column(Unicode(36), default=lambda : str(uuid4()), unique=True)
    command_type = Column(Unicode(1024))
    command_date = Column(UnicodeText)
    identity = Column(Unicode(1024))


class RegisteredTool(Base):
    name = Column('name', Unicode(1024), unique=True)
    options = Column('options', MutableDict.as_mutable(JSONEncodedDict))
    help_str = Column('help', UnicodeText)
    section = Column('section', UnicodeText)