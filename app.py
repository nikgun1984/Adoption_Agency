from flask import Flask, redirect, render_template, request, flash
from models import db, connect_db, Pet
from flask_debugtoolbar import DebugToolbarExtension
from forms import AddPetForm

app = Flask(__name__)

#Configurations
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///pets'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = 'whateverpassword'
app.config["SEND_FILE_MAX_AGE_DEFAULT"] = 0
app.config["DEBUG_TB_HOSTS"] = ["dont-show-debug-toolbar"]

"""Debugger Initialization"""
debug  = DebugToolbarExtension(app)

#Connect to Database and create all tables
connect_db(app)
db.create_all()

@app.route('/')
def list_pets():
    pets = db.session.query(Pet).all()
    return render_template('list_pets.html', pets = pets)

@app.route('/pets/add', methods=["GET","POST"])
def add_pet():
    form = AddPetForm()
    if form.validate_on_submit():
        name = form.name.data
        species = form.species.data
        photo = form.photo.data
        age =form.age.data
        notes = form.notes.data
        is_available = form.available.data

        pet = Pet(name=name,species=species,photo_url=photo,age=age,notes=notes,available=is_available)
        db.session.add(pet)
        db.session.commit()
        flash(f'Created {name} {species}')
        return redirect('/')
    return render_template('add_pet.html',form=form)