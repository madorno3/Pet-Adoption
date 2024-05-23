# from flask import Flask, render_template, redirect, flash, session
# from flask_debugtoolbar import DebugToolbarExtension
# from models import db, connect_db, Pet
# # from forms import 

# app = Flask(__name__)



# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///adopt'
# app.config['SQLALCHEMY_ECHO'] = False
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# # app.config['SECRET_KEY'] = "abc123"

# app.app_context().push()
# connect_db(app)



# toolbar = DebugToolbarExtension(app)
from flask import Flask, render_template, redirect, flash, session
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, Pet

app = Flask(__name__)

# Generate a new secret key for your application
app.config['SECRET_KEY'] = 'harleyquinn'  # Replace 'your-secret-key-here' with a real secret key

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///adopt'
app.config['SQLALCHEMY_ECHO'] = False
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['DEBUG'] = True  # Enable debug mode
app.app_context().push()
with app.app_context():
    connect_db(app)  # Ensure the app context is active when connecting to the database

toolbar = DebugToolbarExtension(app)



import os
SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = "SECRET_KEY"

@app.route("/")
def home():
    return render_template('home.html')