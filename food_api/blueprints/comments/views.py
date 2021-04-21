from flask import Blueprint, json, jsonify, request
import jwt
from models.user import User
from models.image import Image
from models.comment import Comment
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import jwt_required

comments_api_blueprint = Blueprint('comments_api',
                             __name__,
                             template_folder='templates')

@comments_api_blueprint.route('/<id>/comments', methods=['POST'])
@jwt_required()
def index(id):
    identity = get_jwt_identity()
    user = User.get(username=identity)
    image = Image.get_by_id(id)
    user_comment = request.json.get("comment")
    if user:
        comment = Comment(user=user.id, image=image.id, user_comment=user_comment)
        if comment.save():
            return jsonify({'message' : 'success'})
        else:
            return jsonify({'message' : 'failed'})
    else:
        return jsonify({'message' : 'User Not Found'})

@comments_api_blueprint.route('/comments_delete/<id>', methods=['POST'])
@jwt_required()
def destroy(id):
    comment = Comment.get_by_id(id)
    if comment.delete_instance():
        return jsonify({'message' : 'success'})
    else:
        return jsonify({'message' : 'failed'})
