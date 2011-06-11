from stormbb.models import User, Category, Board, Topic, Message
from pyramid.view import view_config

def includeme(config):
    config.scan(__name__)
    config.add_route('index', '')

@view_config(route_name='index', renderer='index.mak')
def index(request):
    # for now, just get the first category and boards.
    cat = Category.objects.order_by('order').first()
    return dict(categories=[cat])
