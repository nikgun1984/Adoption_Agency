from flask import Flask, redirect, render_template, request
from models import db, connect_db, Pet
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)

#Configurations
app.config['SLQALCHEMY_DATABASE_URI'] = 'postgresql:///pet'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = 'whateverpassword'
app.config["SEND_FILE_MAX_AGE_DEFAULT"] = 0
app.config["DEBUG_TB_HOSTS"] = ["dont-show-debug-toolbar"]

"""Debugger Initialiqzation"""
debug  = DebugToolbarExtension(app)

#Connect to Database and create all tables
connect_db(app)
db.create_all()