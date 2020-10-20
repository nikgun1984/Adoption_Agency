from flask import Flask, redirect, render_template, request
from models import db, connect_db, Pet
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)

#Configurations
app.config['SLQALCHEMY_DATABASE_URI'] = 'postgresql:///pets'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = 'whateverpassword'
# app.config["SEND_FILE_MAX_AGE_DEFAULT"] = 0
# app.config["DEBUG_TB_HOSTS"] = ["dont-show-debug-toolbar"]

"""Debugger Initialization"""
debug  = DebugToolbarExtension(app)

#Connect to Database and create all tables
connect_db(app)
db.drop_all()
db.create_all()

# app.route('/')
# def list_pets():
#     # db.session.query(Pet).
#     return render_template('home.html', pets = pets)