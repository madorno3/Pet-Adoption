
from flask import Flask, request, render_template, redirect, flash, session
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, Pet
from sqlalchemy.orm import Session 
from forms import PetForm, EditPetForm

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///adopt'
app.config['SQLALCHEMY_ECHO'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['DEBUG'] = True  
app.config['SECRET_KEY'] = 'harleyquinn' 
app.app_context().push()

connect_db(app)  
db.create_all()

toolbar = DebugToolbarExtension(app)

import os
SECRET_KEY = os.urandom(32)

@app.route("/")
def home():
    pets = Pet.query.all()
    return render_template('home.html',pets=pets)

@app.route("/add_pet_form", methods=["GET", "POST"])
def add_pet():
    form = PetForm()
    if form.validate_on_submit():
        new_pet = Pet(name=form.name.data, species=form.species.data, photo_url=form.photo.data, age=form.age.data, notes=form.notes.data)
        db.session.add(new_pet)
        db.session.commit()
        return redirect('/')

    return render_template('add_pet_form.html', form=form)

@app.route("/<int:pet_id>", methods=["GET", "POST"])
def pet_details(pet_id):
    pet = Pet.query.get_or_404(pet_id)
    form = EditPetForm()
    if form.validate_on_submit():
        pet.notes = form.notes.data
        pet.available = form.available.data
        pet.photo_url = form.photo_url.data
        db.session.commit()
        flash(f"{pet.name} updated.")
        return redirect("/")
    return render_template("pet_bio.html",form=form, pet=pet)
