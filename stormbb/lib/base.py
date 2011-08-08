"""The base Controller API

Provides the BaseController class for subclassing.
"""
from stormbb.model import User
from stormbb.lib import facebook
from pylons import config, request, response
from pylons.controllers import WSGIController
from pylons.controllers.util import redirect
from pylons.templating import render_mako as render


class AnonymousUser(object):
    """A dummy class used to identify an anonymous user.
    """
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

        # check facebook cookies first
        fb_cookie = facebook.get_user_from_cookie(request.cookies,
                                                  config['facebook.app_id'],
                                                  config['facebook.app_secret'])
        if fb_cookie:
            request.fb_cookie = fb_cookie
            try:
                user = User.objects.get(fb_user_id=fb_cookie['uid'])
            except User.DoesNotExist, e:
                # redirect to facebook signup page if we are not already there
                signup_path = '/auth/facebook/new'
                if not request.path == signup_path:
                    redirect(signup_path)

            if not user.fb_access_token == fb_cookie['access_token']:
                user.fb_access_token = fb_cookie['access_token']
                user.save()

            request.user = user
