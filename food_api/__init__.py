from operator import imod
from app import app
from flask_cors import CORS

cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

## API Routes ##
from food_api.blueprints.users.views import users_api_blueprint
from food_api.blueprints.sessions.views import sessions_api_blueprint
from food_api.blueprints.images.views import images_api_blueprint
from food_api.blueprints.follows.views import follows_api_blueprint
from food_api.blueprints.catalogue.views import catalogue_api_blueprint
from food_api.blueprints.grocerylists.views import grocerylists_api_blueprint
from food_api.blueprints.comments.views import comments_api_blueprint
from food_api.blueprints.likes.views import likes_api_blueprint

app.register_blueprint(users_api_blueprint, url_prefix='/api/v1/users')
app.register_blueprint(sessions_api_blueprint, url_prefix='/api/v1')
app.register_blueprint(images_api_blueprint, url_prefix='/api/v1/images')
app.register_blueprint(follows_api_blueprint, url_prefix='/api/v1')
app.register_blueprint(catalogue_api_blueprint, url_prefix='/api/v1/catalogue')
app.register_blueprint(grocerylists_api_blueprint, url_prefix='/api/v1/grocerylists')
app.register_blueprint(comments_api_blueprint, url_prefix='/api/v1/images')
app.register_blueprint(likes_api_blueprint, url_prefix='/api/v1')
