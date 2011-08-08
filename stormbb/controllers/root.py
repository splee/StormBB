import logging

from pylons import request, response, session, tmpl_context as c, url
from pylons.controllers.util import abort, redirect

from stormbb.lib.base import BaseController, render
from stormbb.model import Board, Category

log = logging.getLogger(__name__)

class RootController(BaseController):

    def index(self):
        boards = Board.objects(read_groups__in=request.user.groups)
        cat_ids = [cat.id for cat in boards.distinct('category')]
        c.categories = Category.objects(id__in=cat_ids).order_by('order')
        return render('/index.mako')
