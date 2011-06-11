from stormbb.resources import Root
from stormbb.views import user, root
from pyramid.config import Configurator
from pyramid.authentication import AuthTktAuthenticationPolicy
from pyramid.authorization import ACLAuthorizationPolicy

from mongoengine import connect

def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    def get_groups(user_id, request):
        identity = authn.cookie.identify(request)
        if identity:
            return identity['tokens'][1:]

    def renderer_globals(system):
        identity = authn.cookie.identify(system['request'])
        if identity:
            user_id = identity['userid']
            display_name, groups = user.parse_tokens(identity['tokens'])
        else:
            user_id = None
            display_name = u''
            groups = []
        return dict(USER_ID=user_id,
                    USER_DISPLAY_NAME=display_name,
                    USER_GROUPS=groups)

    authn = AuthTktAuthenticationPolicy('This is a secret. No, really... it is!',
                                        callback=get_groups)
    authz = ACLAuthorizationPolicy()

    config = Configurator(root_factory=Root,
                          settings=settings,
                          renderer_globals_factory=renderer_globals,
                          authentication_policy=authn,
                          authorization_policy=authz)
    #config.add_view('stormbb.views.my_view',
    #                context='stormbb:resources.Root',
    #                renderer='stormbb:templates/index.mak')

    config.add_static_view('static', 'stormbb:static')

    # root views
    config.include(root)
    # user routes
    config.include(user)

    # set up db
    #db_uri = settings['db_uri']
    #db_name = settings['db_name']
    #connect(db_name)
    return config.make_wsgi_app()

