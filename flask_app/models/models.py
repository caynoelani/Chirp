#******************************************************
#***********************IMPORTS************************
#******************************************************

#=====================================
# General Imports
#=====================================
from flask_app import db
from datetime import datetime


#******************************************************
#*****************ASSOCIATION TABLES*******************
#******************************************************

#=====================================
# Bookmark
#=====================================
bookmarks = db.Table('bookmarks',
    db.Column('id', db.Integer, primary_key=True, autoincrement=True),
    db.Column('created_at', db.Date, default=datetime.utcnow),
    db.Column('update_at', db.Date, default=datetime.utcnow),

    db.Column('post_id', db.Integer, db.ForeignKey('post.id')),
    db.Column('user_id', db.Integer, db.ForeignKey('user.id')),
)


#=====================================
# Follow
#=====================================
follows = db.Table('follows',
    db.Column('id', db.Integer, primary_key=True, autoincrement=True),
    db.Column('created_at', db.Date, default=datetime.utcnow),
    db.Column('update_at', db.Date, default=datetime.utcnow),

    db.Column('follower_id', db.Integer, db.ForeignKey('user.id')),
    db.Column('followee_id', db.Integer, db.ForeignKey('user.id')),
)


#=====================================
# Like
#=====================================
likes = db.Table('likes',
    db.Column('id', db.Integer, primary_key=True, autoincrement=True),
    db.Column('created_at', db.Date, default=datetime.utcnow),
    db.Column('updated_at', db.Date, default=datetime.utcnow),

    db.Column('repost_id', db.Integer, db.ForeignKey('repost.id')),
    db.Column('user_id', db.Integer, db.ForeignKey('user.id')),
    db.Column('post_id', db.Integer, db.ForeignKey('post.id')),
    db.Column('comment_id', db.Integer, db.ForeignKey('comment.id')),
)



#******************************************************
#***********************MODELS*************************
#******************************************************

#=====================================
# Comment
#=====================================
class Comment(db.Model):
    __tablename__ = 'comments'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    comment = db.Comlumn(db.String(255), nullable=False)
    created_at = db.Column(db.Date, default=datetime.utcnow)
    update_at = db.Column(db.Date, default=datetime.utcnow)

    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    post_id = db.Column(db.Integer, db.ForeignKey('post.id'))
    repost_id = db.Column(db.Integer, db.ForeignKey('repost.id'))

    likes = db.relationship('Like', secondary=likes, backref='comment')


#=====================================
# Post
#=====================================
class Post(db.Model):
    __tablename__ = 'posts'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    chirp = db.Comlumn(db.String(255), nullable=False)
    created_at = db.Column(db.Date, default=datetime.utcnow)
    update_at = db.Column(db.Date, default=datetime.utcnow)

    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    bookmarks = db.relationship('Bookmark', secondary=bookmarks,backref='post')
    comments = db.relationship('Comment', backref='post')
    likes = db.relationship('Like', secondary=likes, backref='post')
    reposts = db.relationship('Repost', backref='post')


#=====================================
# Repost
#=====================================
class Repost(db.Model):
    __tablename__ = 'reposts'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    text = db.Comlumn(db.String(255))
    created_at = db.Column(db.Date, default=datetime.utcnow)
    update_at = db.Column(db.Date, default=datetime.utcnow)

    post_id = db.Column(db.Integer, db.ForeignKey('post.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    comments = db.relationship('Comment', backref='repost')
    likes = db.relationship('Like', secondary=likes, backref='repost')


#=====================================
# User
#=====================================
class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
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

    bookmarks = db.relationship('Bookmark', secondary=bookmarks,backref='user')
    comments = db.relationship('Comment', backref='user')
    follower = db.relationship('User', secondary=follows, backref='followees')
    followees= db.relationship('User', secondary=follows, backref='followers')
    likes = db.relationship('Like', secondary=likes, backref='user')
    posts = db.relationship('Post', backref='user')
    reposts = db.relationship('Repost', backref='user')

    def __repr__(self):
        return f'User: {self.username}'