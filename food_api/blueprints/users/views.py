from flask import Blueprint, json, jsonify, request
from models.user import User
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import jwt_required

users_api_blueprint = Blueprint('users_api',
                             __name__,
                             template_folder='templates')

@users_api_blueprint.route('/', methods=['GET'])
def index():
    users = User.select()
    results = []

    for user in users:
        results.append(
            {
                "id" : user.id,
                "username" : user.username,
                "email" : user.email,
                "profile_image" : user.profile_image
            }
        )
    return jsonify(results)

@users_api_blueprint.route('/<id>', methods=['GET'])
def user(id):
    user = User.get_by_id(id)
    user_data = {}
    user_data['id'] = user.id
    user_data['username'] = user.username
    user_data['email'] = user.email
    user_data['profile_image'] = user.profile_image
    return jsonify(user_data)

@users_api_blueprint.route('/me', methods=['GET'])
@jwt_required()
def me():
    identity = get_jwt_identity()
    user = User.get(username=identity)
    user_data = {}
    user_data['id'] = user.id
    user_data['username'] = user.username
    user_data['email'] = user.email
    user_data['profile_image'] = user.profile_image
    return jsonify(user_data)

@users_api_blueprint.route('/signup', methods=['POST'])
def sign_up():
    username = request.json.get("username")
    email = request.json.get("email")
    password = request.json.get("password")
    user = User(username=username, email=email, password=password)
    if user.save():
        return jsonify({'success' : True})
    else:
        return jsonify({'errors' : user.errors})

@users_api_blueprint.route('/update/<id>', methods=['POST'])
def update(id):
    user = User.get_or_none(User.id == id)
    if user:
        username = request.json.get("username")
        email = request.json.get("email")
        password = request.json.get("password")
        if username:
            user.username = username
        if email:
            user.email = email
        if password:
            user.password = password
        if user.save():
            return jsonify({'message' : 'success'})
        else:
            return jsonify({'errors' : user.errors})
    else:
        return jsonify({'message' : 'User Does Not Exist'})