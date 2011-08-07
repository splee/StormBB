from mongoengine import connect
from user import User
from forums import Category, Board, Topic, Message

# connect
# TODO: Use settings for this

connect('stormbb')
