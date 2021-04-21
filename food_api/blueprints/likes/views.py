from flask import Blueprint, json, jsonify, request
from flask_jwt_extended.view_decorators import jwt_required
import jwt
from models.user import User
from models.image import Image
from models.comment import Comment
from models.image_like import ImageLike
from models.comment_like import CommentLike
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import jwt_required

likes_api_blueprint = Blueprint('likes_api',
                             __name__,
                             template_folder='templates')

@likes_api_blueprint.route('/images/<id>/like', methods=['POST'])
@jwt_required()
def like_image(id):
    identity = get_jwt_identity()
    user = User.get(username=identity)
    image = Image.get_by_id(id)
    if user:
        image_like = ImageLike(user=user.id, image=image.id, is_like=True)
        if image_like.save():
            return jsonify({'message' : 'success'})
        else:
            return jsonify({'message' : 'failed'})
    else:
        return jsonify({'message' : 'User Not Found'})

@likes_api_blueprint.route('/images/<id>/unlike', methods=['POST'])
@jwt_required()
def unlike_image(id):
    identity = get_jwt_identity()
    user = User.get(username=identity)
    image = Image.get_by_id(id)
    if user:
        image_like = ImageLike.get(user=user.id, image=image.id, is_like=True)
        image_like.is_like = False
        if image_like.save():
            return jsonify({'message' : 'success'})
        else:
            return jsonify({'message' : 'failed'})
    else:
        return jsonify({'message' : 'User Not Found'})

@likes_api_blueprint.route('/comments/<id>/like', methods=['POST'])
@jwt_required()
def like_comment(id):
    identity = get_jwt_identity()
    user = User.get(username=identity)
    comment = Comment.get_by_id(id)
    if user:
        comment_like = CommentLike(user=user.id, comment=comment.id, is_like=True)
        if comment_like.save():
            return jsonify({'message' : 'success'})
        else:
            return jsonify({'message' : 'failed'})
    else:
        return jsonify({'message' : 'User Not Found'})

@likes_api_blueprint.route('/comments/<id>/unlike', methods=['POST'])
@jwt_required()
def unlike_comment(id):
    identity = get_jwt_identity()
    user = User.get(username=identity)
    comment = Comment.get_by_id(id)
    if user:
        comment_like = CommentLike.get(user=user.id, comment=comment.id, is_like=True)
        comment_like.is_like = False
        if comment_like.save():
            return jsonify({'message' : 'success'})
        else:
            return jsonify({'message' : 'failed'})
    else:
        return jsonify({'message' : 'User Not Found'})