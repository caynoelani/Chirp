#******************************************************
#***********************IMPORTS************************
#******************************************************

#=====================================
# Import app
#=====================================
from flask_app import app

#=====================================
# Import Modules/Packages
#=====================================
from flask import redirect, render_template, session, request
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

#=====================================
# Import Models
#=====================================


#******************************************************
#***********************ROUTES*************************
#******************************************************

#=====================================
# Home Route
#=====================================
@app.route('/', methods=['POST', 'GET'])
def home_page():

    return render_template('index.html')

#=====================================
# Notifications Route
#=====================================
@app.route('/notifications', methods=['POST', 'GET'])
def notifications_page():

    return render_template('notifications.html')

#=====================================
# Mentions Route
#=====================================
@app.route('/notifications/mentions', methods=['POST', 'GET'])
def mentions_page():

    return render_template('mentions.html')

#=====================================
# Bookmarks Route
#=====================================
@app.route('/bookmarks', methods=['POST', 'GET'])
def bookmarks_page():

    return render_template('bookmarks.html')

#=====================================
# Profile Route
#=====================================
@app.route('/profile', methods=['POST', 'GET'])
def profile_page():

    return render_template('profile.html')

#=====================================
# Replies Route
#=====================================
@app.route('/profile/replies', methods=['POST', 'GET'])
def replies_page():

    return render_template('replies.html')