from stormbb.models import User, Category, Board, Topic, Message
from pyramid.view import view_config

def includeme(config):
    config.scan(__name__)
    config.add_route('index', '')
    config.add_route('board', 'board/{board_id}')
    config.add_route('topic', 'topic/{topic_id}')

@view_config(route_name='index', renderer='index.mak')
def index(request):
    # for now, just get the first category and boards.
    cat = Category.objects.order_by('order').first()
    return dict(categories=[cat])

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
