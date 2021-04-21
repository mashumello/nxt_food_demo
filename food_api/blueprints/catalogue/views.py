from flask import Blueprint, json, jsonify, request
import jwt
from models import catalogue
from models.user import User
from models.catalogue import Catalogue
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import jwt_required

catalogue_api_blueprint = Blueprint('catalogue_api', 
                            __name__,
                            template_folder='templates')

@catalogue_api_blueprint.route('/', methods=['POST'])
@jwt_required()
def index():
    identity = get_jwt_identity()
    user = User.get(username=identity)
    ingredient = request.json.get('ingredient')
    if user:
        catalogue = Catalogue(user=user.id, ingredient=ingredient)
        if catalogue.save():
            return jsonify({'message' : 'success'})
        else:
            return jsonify({'message' : 'failed'})
    else:
        return jsonify({'message' : 'User Not Found'})

@catalogue_api_blueprint.route('/delete/<id>', methods=['POST'])
@jwt_required()
def destroy(id):
    catalogue = Catalogue.get_by_id(id)
    if catalogue.delete_instance():
        return jsonify({'message' : 'success'})
    else:
        return jsonify({'message' : 'failed'})

@catalogue_api_blueprint.route('/<id>', methods=['GET'])
def user_catalogue(id):
    user = User.get_or_none(User.id == id)
    results = []
    if user:
        for catalogue in user.catalogues:
            results.append(
                {
                    "catalogue_id" : catalogue.id,
                    "ingredient" : catalogue.ingredient
                }
            )
        return jsonify(results)
    else:
        return jsonify({"message" : "User Does Not Exit"})



