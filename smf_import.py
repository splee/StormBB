import MySQLdb
from stormbb.models import User, Category, Board, Topic, Message
from datetime import datetime

# storage for data
categories = {}
boards = {}
topics = {}
members = {}

conn = None

bad_count = 0

def connect(**kw):
    global conn
    conn = MySQLdb.connect(**kw)

def import_users():
    c = conn.cursor()
    sql = """
SELECT
    ID_MEMBER
    ,memberName
    ,dateRegistered
    ,posts
    ,realName
    ,location
    ,signature
    ,userTitle
    ,passwd
    ,passwordSalt
    ,emailAddress
FROM
    smf_members;"""

    c.execute(sql)
    for row in c.fetchall():
        u = User()
        u.smf_id = row[0]
        u.username = row[1]
        u.registered = datetime.fromtimestamp(row[2])
        u.post_count = row[3]
        u.display_name = row[4]
        u.location = row[5]
        u.signature = row[6]
        u.custom_title = row[7]
        u.password = row[8]
        u.salt = row[9]
        u.email = row[10]
        u.hash_name = 'smf'
        u.save()

        members[u.smf_id] = u

    c.close()

def import_categories():
    c = conn.cursor()
    sql = """
SELECT
    ID_CAT
    ,name
    ,catOrder
FROM
    smf_categories;"""

    c.execute(sql)
    for row in c.fetchall():
        cat = Category()
        cat.name = row[1]
        cat.order = row[2]
        cat.save()

        categories[row[0]] = cat

    c.close()

def import_boards():
    c = conn.cursor()
    sql = """
SELECT
    ID_BOARD
    ,ID_CAT
    ,ID_PARENT
    ,boardOrder
    ,name
    ,description
    ,numTopics
    ,numPosts
FROM
    smf_boards
ORDER BY ID_PARENT;"""

    c.execute(sql)
    for row in c.fetchall():
        b = Board()
        b.category = categories[row[1]]
        if row[2] > 0:
            b.parent = boards[row[2]]
        b.order = row[3]
        b.name = row[4]
        b.description = row[5]
        b.topic_count = row[6]
        b.post_count = row[7]
        b.save()

        boards[row[0]] = b

    c.close()

def import_topics():
    c = conn.cursor()
    sql = """
SELECT
    ID_TOPIC
    ,isSticky
    ,ID_BOARD
    ,numReplies
    ,numViews
    ,locked
    ,ID_MEMBER_STARTED
FROM
    smf_topics;"""

    c.execute(sql)
    for row in c.fetchall():
        t = Topic()
        t.is_sticky = bool(row[1])
        t.board = boards[row[2]]
        t.reply_count = row[3]
        t.view_count = row[4]
        t.is_locked = bool(row[5])
        if row[6] > 0:
            t.creator = members[row[6]]
        t.save()

        topics[row[0]] = t

    c.close()

def import_messages():
    c = conn.cursor()
    sql = """
SELECT
    ID_MSG
    ,ID_TOPIC
    ,ID_BOARD
    ,posterTime
    ,ID_MEMBER
    ,body
    ,subject
FROM
    smf_messages;"""

    c.execute(sql)

    for row in c.fetchall():
        # try cleaning up the data here
        body = row[5].decode('windows-1252')
        title = row[6].decode('windows-1252')

        m = Message()
        m.topic = topics[row[1]]
        m.board = boards[row[2]]
        m.created = datetime.fromtimestamp(row[3])
        if row[4] > 0:
            m.author = members[row[4]]
        m.body = body
        m.title = title

        dirty_topic = False
        if not m.topic.title:
            m.topic.title = title
            dirty_topic = True

        if not m.topic.last_update or m.created > m.topic.last_update:
            m.topic.last_update = m.created
            dirty_topic = True

        if dirty_topic:
            m.topic.save()

        m.save()

    c.close()

def import_all():
    import_users()
    import_categories()
    import_boards()
    import_topics()
    import_messages()
