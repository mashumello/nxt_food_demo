from flask import Blueprint, json, jsonify, request
import jwt
from models.user import User
from models.follow import Follow
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import jwt_required

follows_api_blueprint = Blueprint('follows_api', 
                            __name__,
                            template_folder='templates')

@follows_api_blueprint.route('/follow/<idol_id>', methods=['POST'])
@jwt_required()
def fan(idol_id):
    identity = get_jwt_identity()
    fan = User.get(username=identity)
    idol = User.get_by_id(idol_id)
    if idol:
        if idol.is_private == True:
            follow = Follow(fan=fan, idol=idol, is_approve=False)
            if follow.save():
                return jsonify({'message' : 'success'})
            else:
                return jsonify({'message' : 'failed'})
        else:
            follow = Follow(fan=fan, idol=idol, is_approve=True)
            if follow.save():
                return jsonify({'message' : 'success'})
            else:
                return jsonify({'message' : 'failed'})
    else:
        return jsonify({'message' : 'User Not Found'})

@follows_api_blueprint.route('/follow_request/<id>', methods=['GET'])
def follow_request(id):
    requests = User.select().join(Follow, on=(User.id==Follow.fan)).where(Follow.idol==User.get_by_id(id), Follow.is_approve==False)
    results = []
    for request in requests:
        user_data = {}
        user_data['username'] = request.username
        user_data['email'] = request.email
        user_data['profile_image'] = request.profile_image
        results.append(user_data)
    return jsonify({"follow_request ": results})

@follows_api_blueprint.route('/delete_request/<idol_id>', methods=['POST'])
@jwt_required()
def delete_request(idol_id):
    identity = get_jwt_identity()
    fan = User.get(username=identity)
    idol = User.get_by_id(idol_id)
    request = Follow.get(fan=fan, idol=idol, is_approve=False)
    if request.delete_instance():
        return jsonify({'message' : 'success'})
    else:
        return jsonify({'message' : 'failed'})

@follows_api_blueprint.route('/accept_request/<fan_id>', methods=['POST'])
@jwt_required()
def accept_request(fan_id):
    identity = get_jwt_identity()
    fan = User.get_by_id(fan_id)
    idol = User.get(username=identity)
    request = Follow.get(fan=fan, idol=idol, is_approve=False)
    if request:
        request.is_approve = True
        if request.save():
            return jsonify({'message' : 'success'})
        else:
            return jsonify({'message' : 'failed'})
    else:
        return jsonify({'message' : 'Request Not Found'})

@follows_api_blueprint.route('/decline_request/<fan_id>', methods=['POST'])
@jwt_required()
def decline_request(fan_id):
    identity = get_jwt_identity()
    fan = User.get_by_id(fan_id)
    idol = User.get(username=identity)
    request = Follow.get(fan=fan, idol=idol, is_approve=False)
    if request:
        if request.delete_instance():
            return jsonify({'message' : 'success'})
        else:
            return jsonify({'message' : 'failed'})
    else:
        return jsonify({'message' : 'Request Not Found'})

