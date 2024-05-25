from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, BooleanField, IntegerField, RadioField, SelectField

class PetForm(FlaskForm):

    name =StringField("Pet Name")
    species = StringField("Breed")
    photo = StringField("Photo of pet")
    age = IntegerField()
    notes = StringField("Notes")

class EditPetForm(FlaskForm):
    """Form for editing an existing pet."""
    photo_url = StringField("Photo URL")
    notes = StringField("Comments")
    available = BooleanField("Available?")