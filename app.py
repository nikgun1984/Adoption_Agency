from flask import Flask, redirect, render_template, request, flash, url_for
from models import db, connect_db, Pet
from flask_debugtoolbar import DebugToolbarExtension
from forms import AddPetForm, EditPetInfo
from wtforms.validators import ValidationError
import os

app = Flask(__name__)

#Configurations
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///pets'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = 'whateverpassword'
app.config["SEND_FILE_MAX_AGE_DEFAULT"] = 0
app.config["DEBUG_TB_HOSTS"] = ["dont-show-debug-toolbar"]
app.config["IMAGES_UPLOADS"] = 'static/images/'

"""Debugger Initialization"""
debug  = DebugToolbarExtension(app)

"""Absolute Path for Uploading Images"""
basedir = os.path.abspath(os.path.dirname('__file__'))

#Connect to Database and create all tables
connect_db(app)
db.create_all()

@app.route('/')
def list_pets():
    """will display all animals in the market"""
    pets = db.session.query(Pet).all()
    return render_template('list_pets.html', pets = pets)

@app.route('/pets/add', methods=["GET","POST"])
def add_pet():
    """will display form to add pet and submit this form"""
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

@app.route('/pets/<int:pet_id>', methods=["GET","POST"])
def show_pet(pet_id):
    """edit particular animal/displaying pet's information"""
    pet = Pet.query.get_or_404(pet_id)
    form = EditPetInfo(obj=pet)
    if form.validate_on_submit():
        pet.photo_url = form.photo_url.data
        pet.notes = form.notes.data
        pet.available = form.available.data
        if form.upload.data:
            image = request.files["upload"]
            image.save(os.path.join(basedir,app.config["IMAGES_UPLOADS"],image.filename))
            pet.photo_url = os.path.join('/',app.config["IMAGES_UPLOADS"],image.filename)
        try:
            form.validate_photo_upload(form.photo_url.data,form.upload.data)
            db.session.commit()
            flash("This user was successfully edited...","success")
            return redirect('/')
        except ValidationError as e:
            flash(str(e),"error")
            return redirect(f"/pets/{pet_id}")
    return render_template('display_pet.html',pet=pet, form=form)