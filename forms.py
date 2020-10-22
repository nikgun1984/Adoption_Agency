from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, TextAreaField, BooleanField, SelectField, FileField
from wtforms.validators import InputRequired, Optional, Email, NumberRange, URL, ValidationError, Regexp

class AddPetForm(FlaskForm):
    """form for adding pet to the database"""
    name = StringField("Pet's Name", validators=[InputRequired(message="Pet's Name cannot be blank")])
    species = SelectField('Species', choices=[('cat', 'Cat'), ('dog', 'Dog'), ('porcupine', 'Porcupine')])
    photo = StringField("Photo URL of Pet", validators=[Optional(),URL(require_tld=True, message="Should be a vaild URL")])
    age = IntegerField("Age of Pet",validators=[NumberRange(min=0, max=30, message="Age should be between 0 to 30"),Optional()])
    notes = TextAreaField("Other Notes", validators=[Optional()])
    available = BooleanField("Is Available?")

class EditPetInfo(FlaskForm):
    """update and edit pet's information in the database"""
    photo_url = StringField("Photo URL of Pet", validators=[Optional(),Regexp(r'^(http:|https:|/)(\w|[=+/?.-])*')])
    upload = FileField("Image Upload", validators=[Optional()])
    notes = TextAreaField("Other Notes", validators=[Optional()])
    available = BooleanField("Is Available?")

    def validate_photo_upload(self,photo_url,upload):
        if photo_url and upload:
            raise ValidationError("Photo Upload or PhotoURL fields should be filled, not both...")
    


