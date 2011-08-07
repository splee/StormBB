import mongoengine as e
from datetime import datetime
from postmarkup import render_bbcode

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
        return Topic.objects(board=self).order_by('-is_sticky', '-last_update')


class Topic(e.Document):
    board = e.ReferenceField(Board)
    title = e.StringField()
    is_sticky = e.BooleanField(default=False)
    is_locked = e.BooleanField(default=False)
    creator = e.ReferenceField('User')
    last_author = e.ReferenceField('User')
    last_update = e.DateTimeField()
    reply_count = e.IntField(default=0)
    view_count = e.IntField(default=0)

    def messages(self):
        return Message.objects(topic=self).order_by('created')

class Message(e.Document):
    topic = e.ReferenceField(Topic)
    board = e.ReferenceField(Board)
    author = e.ReferenceField('User')
    created = e.DateTimeField(default=datetime.now)
    title = e.StringField()
    body = e.StringField()
    body_cache = e.StringField()

    @property
    def rendered_body(self):
        if not self.body_cache:
            # SMF seemed to half render the content before it went to the db.
            # Clean it up.
            body = self.body
            body = body.replace('<br />', '\n')
            body = body.replace('&nbsp;', ' ')
            body = body.replace('&quot;', "'")
            body = body.replace('&#039;', "'")
            body = body.replace('&amp;', '&')
            self.body_cache = render_bbcode(body)
            self.save()
        return self.body_cache

