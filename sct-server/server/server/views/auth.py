from cornice.resource import resource, view
from cornice import Service
from pyramid_mailer import get_mailer
from pyramid_mailer.message import Message
import transaction
import datetime
from pyramid.security import remember, forget
from sqlalchemy.exc import SQLAlchemyError
from ..token import generate_confirmation_token, confirm_token
import jsonpickle
from ..models import models
from ..email_template import email_template
import threading
import os, logging
from ..cfg import FILE_REP_TMP

login = Service('login','/login', 'Identify a user on the website')
logout = Service('logout','/logout', 'Logout a user on the website')
register = Service('register', '/register', 'add a new user into the db')
confirm = Service('confirm', '/confirm', 'confirm a user after registration.')
reconfirm = Service('reconfirm', '/reconfirm', 'resend confirm email to a user.')

#The model for this user registration is models.local_user
@register.post()
def register_post(request):
    email = request.json_body['email'].lower()
    password = request.json_body['password']
    country = request.json_body['country']
    occupation = request.json_body['occupation']
    research_center = request.json_body['research_center']

    try:
        session = request.db
        new_user = models.local_user(
        email=email,
        password=password,
        confirmed=False,
        research_center=research_center,
        occupation=occupation,
        country=country
        )
        session.add(new_user)
        session.commit()

    except Exception:
        return {"error":"User already exists"}

    #link to resend activation
    #Add mailler
    mailer = get_mailer(request)
    token = generate_confirmation_token(email)
    decryt = confirm_token(token)


    confirm_url= request.resource_url(request.context, 'confirm', query={'token':token})


    message = Message(subject="Activate your iSCT Account",
                  sender="isctoolbox@gmail.com",
                  recipients=[email],
                  html=email_template(confirm_url)
                      )

    threading._start_new_thread(mailer.send_immediately,(message, False)) #New thread to send email
    # mailer.send_immediately(message, fail_silently=False)

    return {"ok":"New user added to the db"}

@confirm.get()
def confirm_get(request):
    token = request.GET['token']
    email = confirm_token(token)
    print(email)
    session = request.db
    try:
        user = models.local_user.by_mail(email, session)
        if user.confirmed:
            return {'alert':'You are already confirmed!'}
        user.confirmed = True
        # user.confirmed_on = datetime.datetime.now
        session.commit()
        #Create a new folder for the file of the user
        try:
            os.mkdir(os.path.join(FILE_REP_TMP,str(user.id)))
        except FileExistsError:
            logging.error('The folder already exist.')
        return {'ok':'You have confirmed your account. Thanks!'}
    except:
        return {'error':'Wrong token'}


@login.post()
def login_post(request):
    email = request.json_body['email'].lower()
    password = request.json_body['password']

    session = request.db
    user = models.local_user.by_mail(email, session)

    if user and user.verify_password(password):
        if user.confirmed:
            headers = remember(request, user.id)
            request.response.headerlist.extend(headers)
            return {"ok":"Good password","uid":user.id}
        else:
            # print (generate_confirmation_token("po@po.po")) //debug -- can be deleted
            return {'error':'You have to confirmed your account. Click on the link in you mailbox. \n Or resend link:'}
    else:
        headers = forget(request)
        request.response.headerlist.extend(headers)
        return {"error":"Wrong Password or User doesn't exist, please register"}

@logout.get()
def logout_get(request):
    headers = forget(request)
    request.response.headerlist.extend(headers)
    return {'ok':'success logout'}

@reconfirm.get()
def reconfirm_get(request):
    email = request.GET['email'].lower()

    #link to resend activation
    #Add mailler
    mailer = get_mailer(request)
    token = generate_confirmation_token(email)
    decryt = confirm_token(token)

    confirm_url= request.resource_url(request.context, 'confirm', query={'token':token})

    message = Message(subject="Activate your iSCT Account",
                  sender="isctoolbox@gmail.com",
                  recipients=[email],
                  html=email_template(confirm_url)
                      )
    threading._start_new_thread(mailer.send_immediately,(message, False)) #New thread to send email

    return {"ok":"Mail sent"}



'''RESTful users ressources'''
#TODO:restrict for admin user
@resource(collection_path='/users', path='/users/{user_id}')#, permission="authenticated")
class User(object):

    def __init__(self, request):
        self.request = request

    @view(renderer="string")
    def collection_get(self):
        session = self.request.db
        all_user = session.query(models.local_user).all()
        return jsonpickle.dumps(all_user)

    @view(renderer="string")
    def get(self):
        userid = self.request.matchdict['user_id']
        session = self.request.db
        user_selected = session.query(models.local_user).filter_by(id=userid).first()
        return jsonpickle.dumps(user_selected)

    @view()
    def delete(self):
        if (self.request.unauthenticated_userid == 28):
            userid = self.request.matchdict['user_id']
            session = self.request.db
            selected_user = session.query(models.local_user).filter_by(id=userid).first()
            session.delete(selected_user)
            session.commit()
            all_user = session.query(models.local_user).all()
        return {'success':'ok'}

# foobar = Service(name="foobar", path="/foobar")
# @foobar.post(schema=RegisterForm,
#              renderer = 'signup.mako')
# def foobar_post(request):
#     # Process the valid form data, do some work
#     session = request.db
#     new_user = User(first_name=request.validated['first_name'],
#                     last_name=request.validated['last_name'],
#                     email=request.validated['email'],
#                     password=request.validated['password'])
#     session.add(new_user)
#     session.commit()
#     return HTTPFound(location=request.route_url('signin'))
#
#
# @foobar.get(renderer = 'signup.mako')
# def foobar_get(request):
#     schema = RegisterForm()
#     myform = Form(schema, buttons=('Register',))
#     return {"form": myform.render(), "values": None}
#
# @view_config(route_name='signin', renderer='signin.mako')
# def signin(request):
#     schema = SigninForm()
#     submit = deform.Button(name='Sign-in', css_class='btn btn-action text-right signin')
#     myform = Form(schema, buttons=(submit,))
#
#     if 'Sign-in' in request.POST:
#         controls = request.POST.items()
#         try:
#             appstruct = myform.validate(controls)
#         except ValidationFailure as e:
#             return {'form':e.render(), 'values': False}
#         # Process the valid form data, do some work
#         email = appstruct['email']
#         session = request.db
#         if email:
#             user = models.User.by_mail(email, session)
#             if user and user.verify_password(appstruct['password']):
#                 headers = remember(request, user.id)
#             else:
#                 headers = forget(request)
#         else:
#             headers = forget(request)
#         return HTTPFound(location=request.route_url('myfiles'),
#                          headers=headers)
#     # We are a GET not a POST
#     return {"form": myform.render(), "values": None}
#
# @view_config(route_name='signup',
#              renderer='signup.mako')
# def signup(request):
#     schema = RegisterForm()
#     myform = Form(schema, buttons=('Register',))
#
#     if 'Register' in request.POST:
#         controls = request.POST.items()
#         try:
#             appstruct = myform.validate(controls)
#         except ValidationFailure as e:
#             return {'form':e.render(), 'values': False}
#         # Process the valid form data, do some work
#         session = request.db
#         new_user = User(first_name=appstruct['first_name'],
#                         last_name=appstruct['last_name'],
#                         email=appstruct['email'],
#                         password=appstruct['password'])
#         session.add(new_user)
#         session.commit()
#         return HTTPFound(location=request.route_url('signin'))
#
#     # We are a GET not a POST
#     return {"form": myform.render(), "values": None}

# @view_config(route_name='signout', renderer='string')
# def sign_out(request):
#     headers = forget(request)
#     return HTTPFound(location=request.route_url('home'),
#                      headers=headers)\
