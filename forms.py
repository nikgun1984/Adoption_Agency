from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, TextAreaField, BooleanField, SelectField
from wtforms.validators import InputRequired, Optional, Email, NumberRange, URL

class AddPetForm(FlaskForm):

    name = StringField("Pet's Name", validators=[InputRequired(message="Pet's Name cannot be blank")])
    #species = StringField("Species", validators=[InputRequired(message="Do not leave out this Species field blank")])
    species = SelectField('Species', choices=[('cat', 'Cat'), ('dog', 'Dog'), ('porcupine', 'Porcupine')])
    photo = StringField("Photo URL of Pet", validators=[Optional(),URL(require_tld=True, message="Should be a vaild URL")])
    age = IntegerField("Age of Pet",validators=[NumberRange(min=0, max=30, message="Age should be between 0 to 30"),Optional()])
    notes = TextAreaField("Other Notes", validators=[Optional()])
    available = BooleanField("Is Available?")
