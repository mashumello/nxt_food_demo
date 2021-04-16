from flask.json import JSONDecoder
from flask import Blueprint, jsonify, request
import jwt
from models.user import User
from models.image import Image
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import jwt_required
from helpers import s3

images_api_blueprint = Blueprint('images_api',
                            __name__,
                            template_folder='templates')


@images_api_blueprint.route('/<id>', methods=['GET'])
def user_image(id):
    user = User.get_or_none(User.id==id)
    images = Image.select().join(User, on=(User.id==Image.user)).where(Image.user==User.get_by_id(id))
    results = []
    if user:
        for image in user.images:
            results.append(
                {
                    "image_id" : image.id,
                    "image_url" : image.image_url
                }
            )
        return jsonify(results)
    else:

        return jsonify({"message" : "User Does Not Exit"})

@images_api_blueprint.route('/profile_image', methods=['POST'])
@jwt_required()
def upload_profile():
    file = request.files['image']
    bucket_name = "nextagram-aws-bucket"
    s3.upload_fileobj(
        file,
        bucket_name,
        file.filename,
        ExtraArgs={
            "ACL": "public-read",
            "ContentType": file.content_type
        }
    )
    identity = get_jwt_identity()
    user = User.get(username=identity)
    user.profile_image = f"https://{bucket_name}.s3-ap-southeast-1.amazonaws.com/{file.filename}"
    if user.save():
        return jsonify({'message' : 'Image Uploaded'})
    else:
        return jsonify({'errors' : user.errors})

@images_api_blueprint.route('/', methods=['POST'])
@jwt_required()
def upload_image():
    file = request.files['image']
    bucket_name = "nextagram-aws-bucket"
    s3.upload_fileobj(
        file,
        bucket_name,
        file.filename,
        ExtraArgs={
            "ACL": "public-read",
            "ContentType": file.content_type
        }
    )
    identity = get_jwt_identity()
    user = User.get(username=identity)
    image = Image(user=user, image_url=f"https://{bucket_name}.s3-ap-southeast-1.amazonaws.com/{file.filename}")
    if image.save():
        return jsonify({'message' : 'Image Uploaded'})
    else:
        return jsonify({'errors' : user.errors})

@images_api_blueprint.route('/delete/<id>', methods=['POST'])
@jwt_required()
def destroy(id):
    image = Image.get_by_id(id)
    if image.delete_instance():
        return jsonify({'message' : 'success'})

    