from pyramid.config import Configurator
from sqlalchemy import engine_from_config
from sqlalchemy.orm import sessionmaker
from pyramid import authentication, authorization
from .models.models import User
from configparser import ConfigParser
import logging
from .security import get_principals
from pyramid_mailer import Mailer


from pyramid.authentication import AuthTktAuthenticationPolicy
from pyramid.authorization import ACLAuthorizationPolicy
from .security import SecurityFactory

log = logging.getLogger(__name__)

def config_auth_policy(config, settings):
    policy = authentication.AuthTktAuthenticationPolicy(settings['auth_secret'], get_principals, cookie_name="isct_auth", hashalg="sha512")
    config.set_authentication_policy(policy)
    config.set_authorization_policy(authorization.ACLAuthorizationPolicy())

def db(request):
    """every request will have a session associated with it. and will
    automatically rollback if there's any exception in dealing with
    the request
    """
    maker = request.registry.dbmaker
    session = maker()

    def cleanup(request):
        if request.exception is not None:
            session.rollback()
        else:
            session.commit()
        session.close()

    request.add_finished_callback(cleanup)

    return session

def config_plugins(config):
    PluginUpdater(config)

def config_routes(config):

    # config.add_route('404', '/404')
    # config.add_route('403', '/403')
    config.add_route('myfiles','/myfiles',
                 factory='server.security.SecurityFactory')
    config.add_route('displayFile','/display_file',
                 factory='server.security.SecurityFactory')
    config.add_route('deleteFile','/delete_file',
                 factory='server.security.SecurityFactory')
    config.add_route('brainbrowser','/viewer')
    config.add_route('upload','/upload',
                 factory='server.security.SecurityFactory')
    config.add_route('upload_nii','/upload_nii',
                 factory='server.security.SecurityFactory')
    config.add_route('contact','/contact')

    config.add_route('app','/app') #AngularJS test application
    config.add_route('generate_ajax_data', '/ajax_view') #Ajax test request
    config.add_route('homee', '/homee') #Ajax test button
    config.add_route('signin','/signin')
    config.add_route('signout','/signout')
    config.add_route('toolbox','/toolbox')
    config.add_route('signup','/signup')
    config.add_route('auth', '/sign/{action}')
    config.scan()
    config.add_route("api", '/api/*traverse')

def config_db(config, settings):
    # configure database with variables sqlalchemy.*
    engine = engine_from_config(settings, prefix="sqlalchemy.")
    config.registry.dbmaker = sessionmaker(bind=engine)

    # add db session to request
    config.add_request_method(db, reify=True)

def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    config = Configurator(settings=settings)
    config.include('pyramid_chameleon')
    config.include('pyramid_mako')
    config.include("cornice")
    config.include('pyramid_mailer')
    config.registry['mailer'] = Mailer.from_settings(settings)
    config_db(config, settings)
    config_routes(config)
    config_auth_policy(config, settings)

    config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_route('home', '/home')
    config.scan()

    # Added these lines
    ## Pull in Angular App as python package, must have includeme() in __init__.py
    config.include('app')
    ## These pull along with static.py mount the angular app at /
    config.add_route('catchall_static', '/*subpath')
    config.add_view('server.static.static_view', route_name='catchall_static')

    return config.make_wsgi_app()
