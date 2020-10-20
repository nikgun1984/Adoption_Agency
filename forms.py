from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, TextAreaField, BooleanField
from wtforms.validators import InputRequired, Optional, Email

class AddPetForm(FlaskForm):

    name = StringField("Pet's Name", validators=[InputRequired(message="Pet's Name cannot be blank")])
    species = StringField("Species", validators=[InputRequired(message="Do not leave out this Species field blank")])
    photo = StringField("Photo URL of Pet", validators=[Optional()])
    age = IntegerField("Age of Pet",validators=[Optional()])
    notes = TextAreaField("Other Notes", validators=[Optional()])
    available = BooleanField("Is Available?")
