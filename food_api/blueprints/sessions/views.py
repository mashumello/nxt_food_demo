from flask.json import JSONDecoder
from flask import Blueprint, jsonify, request
from models.user import User
from werkzeug.security import check_password_hash
from flask_jwt_extended import create_access_token
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import jwt_required

sessions_api_blueprint = Blueprint('sessions_api',
                            __name__,
                            template_folder='templates')

@sessions_api_blueprint.route('/login', methods=['POST'])
def login():
    username = request.json.get("username", None)
    password = request.json.get("password", None)
    user = User.get_or_none(User.username == username) 
    if user:
        result = check_password_hash(user.hash_password, password)
        if result:
            access_token = create_access_token(identity=username)
            return jsonify(access_token=access_token)
    else:
        return jsonify({'message' : 'No User Found'})

@sessions_api_blueprint.route('/logout', methods=['POST'])
def logout():
    pass