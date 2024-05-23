from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def connect_db(app):
    db.app = app
    db.init_app(app)

class Pet(db.Model):
    """Department. A department has many employees."""

    __tablename__ = "pets"

    pet_id = db.Column(db.Integer,
                   primary_key=True,
                   autoincrement=True)
    name = db.Column(db.Text, nullable=False, unique=False)
    species = db.Column(db.Text, nullable=False, unique=False)
    photo_url= db.Column(db.Text, nullable=True, unique=False)
    age = db.Column(db.Integer, nullable=True, unique=False)
    notes = db.Column(db.Text, nullable=True, unique=False)
    available = db.Column(db.Boolean, nullable=False, default=True)
