#******************************************************
#***********************IMPORTS************************
#******************************************************

#=====================================
# Import app
#=====================================
from flask_app import app, debug

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
# Login/Register Route
#=====================================
@app.route('/login', methods=['POST', 'GET'])
def login_page():

    return render_template('login.html')

app.after_request(debug.sql_debug)