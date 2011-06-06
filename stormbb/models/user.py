import mongoengine as e
from datetime import datetime

class User(e.Document):
    smf_id = e.IntField()
    username = e.StringField(max_length=200, unique=True)
    display_name = e.StringField(max_length=200, required=True)
    email = e.EmailField(unique=True)
    custom_title = e.StringField(max_length=200)
    location = e.StringField(max_length=200)
    signature = e.StringField()
    avatar = e.URLField()

    registered = e.DateTimeField(default=datetime.now)
    last_login = e.DateTimeField(default=datetime.now)
    post_count = e.IntField(default=0)
    pm_count = e.IntField(default=0)

    password = e.StringField(max_length=64)
    salt = e.StringField(max_length=10)
    hash_name = e.StringField(default='sha256')

class Group(e.Document):
    name = e.StringField()
