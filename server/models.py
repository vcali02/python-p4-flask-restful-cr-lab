from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_serializer import SerializerMixin

db = SQLAlchemy()

class Plant(db.Model, SerializerMixin):
    __tablename__ = 'plants'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    image = db.Column(db.String)
    price = db.Column(db.Float)

    def __repr__(self):
        return f'<Plant {self.name} | Price: {self.price}>'

#EX INSTANCE OF CLASS
#sunflower = Plant("sunflower", image, 3.50)
#sunflower.price
#3.50 

#to_dict()
# {"name": "Sunflower",
# "image": "image here",
# "price": "3.50"
#}