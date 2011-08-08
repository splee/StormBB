import mongoengine as e
from datetime import datetime
import hashlib

class TwitterAuth(e.Document):
    user_id = e.IntField(unique=True)
    screen_name = e.StringField()
    access_token = e.StringField()
    access_token_secret = e.StringField()

class FacebookAuth(e.Document):
    user_id = e.StringField(unique=True)
    display_name = e.StringField()
    access_token = e.StringField()

class User(e.Document):
    smf_id = e.IntField()
    username = e.StringField(max_length=200, unique=True)

    facebook_auth = e.ReferenceField(FacebookAuth)
    twitter_auth = e.ReferenceField(TwitterAuth)

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

    groups = e.ListField(e.StringField(), default=lambda: ['everyone'])

    is_admin = e.BooleanField(default=False)

    def verify_password(self, passwd):
        """Returns True if the password was correct, False if not.
        """
        # NOTE: This is the shitty SMF encryption. We will switch to OAuth.
        pwhash = hashlib.sha1(self.username.lower() + passwd).hexdigest()
        return pwhash == self.password
