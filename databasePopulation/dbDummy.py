from app import User, Post
from app import db

# test_user = User(username = 'test_user', email='medhahatesme@gmail.com', password = 'Night04Monkey$')

# db.session.add(test_user)
# db.session.commit()

def get_all_Users():
    return User.query.all()

def get_local_User():
    return User.query.first()

def get_filtered_Users():
    return User.query.filter_by(username = 'test_user').all()

def get_User_ID(user):
    return user.id

def get_User_Posts(user):
    return user.posts
