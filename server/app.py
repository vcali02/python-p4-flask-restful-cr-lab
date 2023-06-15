#!/usr/bin/env python3

from flask import Flask, jsonify, request, make_response
from flask_migrate import Migrate
from flask_restful import Api, Resource

from models import db, Plant

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///plants.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = True

migrate = Migrate(app, db)
db.init_app(app)

api = Api(app)

class Plants(Resource):
    def get(self):
        #STEP 1: query
        plants = [plant.to_dict() for plant in Plant.query.all()]
        #STEP 2: res to JSON obj
        response = make_response(
            jsonify(plants),
            200
        )
        #STEP 3: return res
        return response
    
    def post(self):

        data = request.get_json()

        new_plant = Plant(
            name=data["name"],
            image=data["image"],
            price=data["price"],
        )

        db.session.add(new_plant)
        db.session.commit()

        new_plant_dict = new_plant.to_dict()

        response = make_response(
            jsonify(new_plant_dict),
            201
        )

        return response
#STEP 4: add resource
#this is what we're doing instead of the decorator
api.add_resource(Plants, '/plants')


class PlantByID(Resource):
    def get(self, id):
        #STEP 1: query
        plant = Plant.query.filter_by(id=id).first()
        plant_dict = plant.to_dict()
        #STEP 2: turn res to JSON obj
        response = make_response(
            jsonify(plant_dict),
            200
        )
        #STEP 3: return response
        return response
#STEP 4: add resource
api.add_resource(PlantByID, '/plants/<int:id>')
        

if __name__ == '__main__':
    app.run(port=5555, debug=True)
