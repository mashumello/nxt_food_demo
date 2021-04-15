from flask import Blueprint, json, jsonify, request
from models.user import User

users_api_blueprint = Blueprint('users_api',
                             __name__,
                             template_folder='templates')

@users_api_blueprint.route('/', methods=['GET'])
def index():
    users = User.select()
    results = []

    for user in users:
        user_data = {}
        user_data['id'] = user.id
        user_data['username'] = user.username
        user_data['email'] = user.email
        user_data['profile_image'] = user.profile_image
        results.append(user_data)
    return jsonify({'users' : results})

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
        user.save()
        return jsonify({'success' : True})
    else:
        return jsonify({'message' : 'User Does Not Exist'})