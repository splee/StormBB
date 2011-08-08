"""The base Controller API

Provides the BaseController class for subclassing.
"""
from stormbb.model import User, FacebookAuth
from stormbb.lib import facebook
from pylons import config, request, response, tmpl_context
from pylons.controllers import WSGIController
from pylons.controllers.util import redirect
from pylons.templating import render_mako as render

signup_path_base = '/auth/facebook'
signup_path = "%s/new" % signup_path_base
def redirect_to_signup():
    if not request.path.startswith(signup_path_base):
        redirect(signup_path)

class AnonymousUser(object):
    """A dummy class used to identify an anonymous user.
    """
    username = '__ANONYMOUS__'
    groups = ['everyone']

class BaseController(WSGIController):

    def __call__(self, environ, start_response):
        """Invoke the Controller"""
        # WSGIController.__call__ dispatches to the Controller method
        # the request is routed to. This routing information is
        # available in environ['pylons.routes_dict']
        return WSGIController.__call__(self, environ, start_response)

    def __before__(self):
        # set up the default values
        request.user = AnonymousUser()
        request.fb_cookie = None
        request.fb_auth = None

        # check facebook cookies first
        fb_cookie = facebook.get_user_from_cookie(request.cookies,
                                                  config['facebook.app_id'],
                                                  config['facebook.app_secret'])
        if fb_cookie:
            request.fb_cookie = fb_cookie
            # get the facebook auth object
            fb_auth, created = FacebookAuth.objects.get_or_create(user_id=fb_cookie['uid'])
            request.fb_auth = fb_auth

            if not fb_auth.access_token == fb_cookie['access_token']:
                fb_auth.access_token = fb_cookie['access_token']
                fb_auth.save()

            try:
                user = User.objects.get(facebook_auth=fb_auth)
                request.user = user
            except User.DoesNotExist, e:
                redirect_to_signup()

        tmpl_context.user = request.user
