from models import Pet, db

db.drop_all()
db.create_all()

Harley = Pet(name = "Harley", species = "Pitbull", age="unknown", notes="cute and cuddly", available="True")

db.session.add(Harley)
db.session.commit()