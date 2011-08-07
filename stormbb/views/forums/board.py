from stormbb.models import Board
from pyramid.view import view_config

def includeme(config):
    config.scan(__name__)
    config.add_route('board_get', 'forums/boards/{board_id}')

@view_config(route_name='board_index', renderer='forums/board_index.mak')
def index(request):
    boards = Board.objects
    return boards

@view_config(route_name='board_get', renderer='forums/board_get.mak')
def get(request):
    board_id = request.matchdict['board_id']
    board = Board.objects.with_id(board_id)
    return board

@view_config(route_name='board_post', renderer='forums/board_post.mak')
def post(request):
    pass

@view_config(route_name='board_put', renderer='forums/board_put.mak')
def put(request):
    pass

@view_config(route_name='board_delete', renderer='forums/board_delete.mak')
def delete(request):
    pass
