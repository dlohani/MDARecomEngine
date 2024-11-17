from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_redis import Redis

# Initialize the app
app = Flask(__name__)
app.config.from_object('config.Config')

# Initialize the database
db = SQLAlchemy(app)

# Initialize Redis for caching
redis = Redis(app)

# Import routes and services
from app.api.recommendation_service import bp as recommendation_bp
app.register_blueprint(recommendation_bp)

if __name__ == '__main__':
    app.run(debug=True)
