#******************************************************
#***********************IMPORTS************************
#******************************************************

#=====================================
# General Imports
#=====================================
from flask_app import db
from datetime import datetime

#******************************************************
#***********************MODELS************************
#******************************************************

#=====================================
# Bookmark
#=====================================
class Bookmark(db.Model):
    __tablename__ = 'bookmarks'
    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.Date, default=datetime.utcnow)
    update_at = db.Column(db.Date, default=datetime.utcnow)

    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    post_id = db.Column(db.Integer, db.ForeignKey('post.id'))

#=====================================
# Comment
#=====================================
class Comment(db.Model):
    __tablename__ = 'comments'
    id = db.Column(db.Integer, primary_key=True)
    comment = db.Comlumn(db.String(255), nullable=False)
    created_at = db.Column(db.Date, default=datetime.utcnow)
    update_at = db.Column(db.Date, default=datetime.utcnow)

    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    post_id = db.Column(db.Integer, db.ForeignKey('post.id'))
    repost_id = db.Column(db.Integer, db.ForeignKey('repost.id'))

    likes = db.relationship('Like', backref='comment')

#=====================================
# Follow
#=====================================
class Follow(db.Model):
    __tablename__ = 'follows'
    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.Date, default=datetime.utcnow)
    update_at = db.Column(db.Date, default=datetime.utcnow)

    follower_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    followee_id = db.Column(db.Integer, db.ForeignKey('user.id'))

#=====================================
# Like
#=====================================
class Like(db.Model):
    __tablename__ = 'likes'
    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.Date, default=datetime.utcnow)
    update_at = db.Column(db.Date, default=datetime.utcnow)

    repost_id = db.Column(db.Integer, db.ForeignKey('repost.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    post_id = db.Column(db.Integer, db.ForeignKey('post.id'))
    comment_id = db.Column(db.Integer, db.ForeignKey('comment.id'))


#=====================================
# Post
#=====================================
class Post(db.Model):
    __tablename__ = 'posts'
    id = db.Column(db.Integer, primary_key=True)
    chirp = db.Comlumn(db.String(255), nullable=False)
    created_at = db.Column(db.Date, default=datetime.utcnow)
    update_at = db.Column(db.Date, default=datetime.utcnow)

    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    bookmarks = db.relationship('Bookmark', backref='post')
    comments = db.relationship('Comment', backref='post')
    likes = db.relationship('Like', backref='post')
    reposts = db.relationship('Repost', backref='post')


#=====================================
# Repost
#=====================================
class Repost(db.Model):
    __tablename__ = 'reposts'
    id = db.Column(db.Integer, primary_key=True)
    text = db.Comlumn(db.String(255))
    created_at = db.Column(db.Date, default=datetime.utcnow)
    update_at = db.Column(db.Date, default=datetime.utcnow)

    post_id = db.Column(db.Integer, db.ForeignKey('post.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    comments = db.relationship('Comment', backref='repost')
    likes = db.relationship('Like', backref='repost')


#=====================================
# User
#=====================================
class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(255))
    last_name = db.Column(db.String(255))
    username = db.Column(db.String(255), unique=True, nullable=False)
    email = db.Column(db.String(255), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    dob = db.Column(db.Date)
    bio = db.Column(db.String(255))
    profile_img = db.Column(db.String(255), default='temporary-profile-placeholder.jpg')
    created_at = db.Column(db.Date, default=datetime.utcnow)
    update_at = db.Column(db.Date, default=datetime.utcnow)

    bookmarks = db.relationship('Bookmark', backref='user')
    comments = db.relationship('Comment', backref='user')
    follows = db.relationship('Follow', backref='user')
    likes = db.relationship('Like', backref='user')
    posts = db.relationship('Post', backref='user')
    reposts = db.relationship('Repost', backref='user')

    def __repr__(self):
        return f'User: {self.username}'