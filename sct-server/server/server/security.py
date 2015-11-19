"""
authentication policy/authorization policy
"""
from .models import models as m
from pyramid import security


def get_principals(user_id, request):
    """
    called by authentication policy
    """
    u = request.db.query(m.local_user).filter_by(id=int(user_id)).first()

    if u:
        return [u, security.Authenticated]
    else:
        return []


from pyramid.security import Allow, Everyone, Authenticated

class SecurityFactory(object):
    __acl__ = [(Allow, Everyone, 'view'),
               (Allow, Authenticated, 'user'), ]

    def __init__(self, request):
        pass
