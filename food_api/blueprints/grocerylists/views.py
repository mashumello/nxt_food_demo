from flask import Blueprint, json, jsonify, request
import jwt
from models.user import User
from models.grocery_list import GroceryList
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import jwt_required

grocerylists_api_blueprint = Blueprint('grocerylists_api', 
                            __name__,
                            template_folder='templates')

@grocerylists_api_blueprint.route('/', methods=['POST'])
@jwt_required()
def index():
    identity = get_jwt_identity()
    user = User.get(username=identity)
    ingredient = request.json.get("ingredient", None)
    if user:
        grocerylist = GroceryList(user=user.id, ingredient=ingredient)
        if grocerylist.save():
            return jsonify({'message' : 'success'})
        else:
            return jsonify({'errors' : grocerylist.errors})
    else:
        return jsonify({'message' : 'User Not Found'})

@grocerylists_api_blueprint.route('/delete/<id>', methods=['POST'])
@jwt_required()
def destroy(id):
    grocerylist = GroceryList.get_by_id(id)
    if grocerylist.delete_instance():
        return jsonify({'message' : 'success'})
    else:
        return jsonify({'message' : 'failed'})

@grocerylists_api_blueprint.route('/<id>', methods=['GET'])
def user_grocerylist(id):
    user = User.get_or_none(User.id == id)
    results = []
    if user:
        for grocerylist in user.grocerylists:
            results.append(
                {
                    "grocerylist_id" : grocerylist.id,
                    "ingredient" : grocerylist.ingredient
                }
            )
        return jsonify(results)
    else:
        return jsonify({"message" : "User Does Not Exit"})