import logging

from pylons import request, response, session, tmpl_context as c, url
from pylons.controllers.util import abort, redirect

from stormbb.lib.base import BaseController, render
from stormbb.lib import facebook
from stormbb.model import User

log = logging.getLogger(__name__)

class FacebookController(BaseController):

    def index(self):
        # Return a rendered template
        #return render('/facebook.mako')
        # or, return a string
        return 'Hello World'

    def new(self):
        cookie = request.fb_cookie
        if not cookie:
            abort(500)

        graph = facebook.GraphAPI(cookie['access_token'])
        c.profile = graph.get_object('me')

        if request.method == 'GET':
            return render('/auth/facebook/new.mako')

        elif request.method == 'POST':
            try:
                username = request.POST['username']
                if not username.strip():
                    # this is dirty, but what the hell
                    raise KeyError("No value is almost the same as no key, right?")
            except KeyError, e:
                c.error = 'Please enter a user name.'
                return render('/auth/facebook/new.mako')

            user = User(fb_user_id=c.profile['id'],
                        fb_access_token=cookie['access_token'],
                        username=username)
            user.save()
            redirect('/')

        # we shouldn't have got here, method not allowed bitches
        abort(405)

    def existing(self):
        cookie = request.fb_cookie
        if not cookie:
            abort(500)

        if not request.method == 'POST':
            abort(405)

        try:
            username = request.POST['username']
            password = request.POST['password']
        except KeyError, e:
            abort(418)

        # get the user by username
        try:
            user = User.objects.get(username=username)
            if not user.verify_password(password):
                raise ValueError("Incorrect password")
        except (ValueError, User.DoesNotExist), e:
            graph = facebook.GraphAPI(cookie['access_token'])
            c.profile = graph.get_object('me')
            c.error = 'Incorrect Username or Password'
            return render('/auth/facebook/new.mako')

        # This user has earned the right to claim their old account.
        user.facebook_auth = request.fb_auth
        user.save()
        redirect('/')

