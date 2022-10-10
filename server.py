#******************************************************
#***********************IMPORTS************************
#******************************************************

#===================================
#  Import App
#===================================
from flask_app import app

#===================================
#  Import dotenv
#===================================
from dotenv import load_dotenv
load_dotenv()

#===================================
#  Import Controllers
#===================================
from flask_app.controllers import user_controller

#******************************************************
#***********************SWITCH*************************
#******************************************************
if __name__ == '__main__':
    app.run(debug=True)