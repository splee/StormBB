from stormbb.resources import Root
from stormbb.views import user
from pyramid.config import Configurator
from pyramid.authentication import AuthTktAuthenticationPolicy
from pyramid.authorization import ACLAuthorizationPolicy

from mongoengine import connect

def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    authn = AuthTktAuthenticationPolicy('This is a secret. No, really... it is!')
    authz = ACLAuthorizationPolicy()
    config = Configurator(root_factory=Root,
                          settings=settings,
                          authentication_policy=authn,
                          authorization_policy=authz)
    config.add_view('stormbb.views.my_view',
                    context='stormbb:resources.Root',
                    renderer='stormbb:templates/index.mak')

    config.add_static_view('static', 'stormbb:static')

    # user routes
    config.include(user)

    # set up db
    #db_uri = settings['db_uri']
    #db_name = settings['db_name']
    #connect(db_name)
    return config.make_wsgi_app()

