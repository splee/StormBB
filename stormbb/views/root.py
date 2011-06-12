from stormbb.models import Category, Board, Topic
from pyramid.view import view_config

def includeme(config):
    config.scan(__name__)
    config.add_route('index', '')
    config.add_route('board', 'board/{board_id}')
    config.add_route('topic', 'topic/{topic_id}')

@view_config(route_name='index', renderer='index.mak')
def index(request):
    if request.user:
        groups = request.user.groups
    else:
        groups = ['everyone']
    boards = Board.objects(read_groups__in=groups)
    cat_ids = [c.id for c in boards.distinct('category')]
    categories = Category.objects(id__in=cat_ids).order_by('order')
    return dict(categories=categories)

@view_config(route_name='board', renderer='board.mak')
def board(request):
    board_id = request.matchdict['board_id']
    board = Board.objects.with_id(board_id)
    return dict(board=board)

@view_config(route_name='topic', renderer='topic.mak')
def topic(request):
    topic_id = request.matchdict['topic_id']
    topic = Topic.objects.with_id(topic_id)
    return dict(topic=topic)
