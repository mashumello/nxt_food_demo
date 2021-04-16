from app import app
from flask_cors import CORS

cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

## API Routes ##
from food_api.blueprints.users.views import users_api_blueprint
from food_api.blueprints.sessions.views import sessions_api_blueprint
from food_api.blueprints.images.views import images_api_blueprint
from food_api.blueprints.follows.views import follows_api_blueprint

app.register_blueprint(users_api_blueprint, url_prefix='/api/v1/users')
app.register_blueprint(sessions_api_blueprint, url_prefix='/api/v1')
app.register_blueprint(images_api_blueprint, url_prefix='/api/v1/images')
app.register_blueprint(follows_api_blueprint, url_prefix='/api/v1')
