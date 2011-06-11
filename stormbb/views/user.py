from pyramid.view import view_config
from pyramid.security import remember, forget
from pyramid.httpexceptions import HTTPFound
from stormbb.models import User
import base64

def includeme(config):
    config.scan(__name__)
    config.add_route('user_login', 'login')
    config.add_route('user_logout', 'logout')

@view_config(route_name='user_login', renderer='login.mak',
             request_method='GET')
@view_config(renderer='login.mak', context='pyramid.exceptions.Forbidden')
def login(request):
    if request.path == request.route_path('user_login'):
        # the user accessed the login page directly
        url = request.params.get('url', '/')
    else:
        # the user was denied access to a resource
        url = request.url
    return dict(url=url)

@view_config(route_name='user_login', renderer='json', request_method='POST')
def process_login(request):
    username = request.params.get('username', '').strip()
    password = request.params.get('password', '').strip()

    if not username or not password:
        return dict(status='error', msg='Empty username or password.')

    auth_error = dict(status='error', msg='Username or password is incorrect.')
    try:
        user = User.objects.get(username=username)
    except User.DoesNotExist, e:
        return auth_error

    if not user.verify_password(password):
        return auth_error

    # set the cookie
    cookie_header = remember(request, str(user.id), tokens=format_tokens(user))
    if not hasattr(request, 'response_headerlist'):
        request.response_headerlist = []
    request.response_headerlist.extend(cookie_header)

    return dict(status='ok', msg='Login successful!')

@view_config(route_name='user_logout')
def logout(request):
    """Logs out the current user.
    """
    next_url = request.params.get('url', '/')
    return HTTPFound(location=next_url, headers=forget(request))

def format_tokens(user):
    """Format user information into a cookie.
    """
    display_name = user.display_name.encode('utf8')
    display_name = 'x' + base64.urlsafe_b64encode(display_name)
    display_name = display_name.replace('=', '+')
    return [display_name] + user.groups

def parse_tokens(tokens):
    """Parse user information from a cookie.
    """
    display_name = tokens[0][1:].replace('+', '=')
    display_name = base64.urlsafe_b64decode(display_name)
    display_name = display_name.decode('utf8')
