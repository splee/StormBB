from stormbb.resources import Root
from stormbb.views import user, root
from stormbb.models import User
from pyramid.config import Configurator
from pyramid.authentication import AuthTktAuthenticationPolicy
from pyramid.authorization import ACLAuthorizationPolicy
from pyramid.decorator import reify
from pyramid.request import Request as PyramidRequest

authn = None
authz = None

class AnonymousUser(object):
    groups = ['everyone']

class Request(PyramidRequest):
    @reify
    def user(self):
        # TODO: Figure out a way of doing this sans globals. --Lee 2011-06-12
        identity = authn.cookie.identify(self)
        if identity:
            user_id = identity['userid']
            if user_id:
                return User.objects.with_id(user_id)
        return AnonymousUser()


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

    # TODO: hacky. I don't like this, but it works for now. --Lee
    global authn
    authn = AuthTktAuthenticationPolicy('This is a secret. No, really... it is!',
                                        callback=get_groups)
    global authz
    authz = ACLAuthorizationPolicy()

    config = Configurator(root_factory=Root,
                          settings=settings,
                          renderer_globals_factory=renderer_globals,
                          authentication_policy=authn,
                          authorization_policy=authz)
    config.set_request_factory(Request)
    config.add_static_view('static', 'stormbb:static')

    # root views
    config.include(root)
    # user routes
    config.include(user)

    return config.make_wsgi_app()

