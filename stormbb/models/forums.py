import mongoengine as e
from datetime import datetime

class Category(e.Document):
    name = e.StringField()
    order = e.IntField()

    def boards(self):
        return Board.objects(category=self).order_by('order')

class Board(e.Document):
    category = e.ReferenceField(Category)
    name = e.StringField()
    order = e.IntField()
    description = e.StringField()
    parent = e.ReferenceField('self')
    topic_count = e.IntField(default=0)
    post_count = e.IntField(default=0)

    read_groups = e.ListField(e.StringField())
    post_groups = e.ListField(e.StringField())
    mod_groups = e.ListField(e.StringField())

    def topics(self):
        return Topic.objects(board=self).order_by('-last_update')

class Topic(e.Document):
    board = e.ReferenceField(Board)
    is_sticky = e.BooleanField(default=False)
    is_locked = e.BooleanField(default=False)
    creator = e.ReferenceField('User')
    last_author = e.ReferenceField('User')
    last_update = e.DateTimeField()
    reply_count = e.IntField(default=0)
    view_count = e.IntField(default=0)

class Message(e.Document):
    topic = e.ReferenceField(Topic)
    board = e.ReferenceField(Board)
    author = e.ReferenceField('User')
    created = e.DateTimeField(default=datetime.now)
    body = e.StringField()
