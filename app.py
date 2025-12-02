import os
from flask import Flask
from flask_cors import CORS
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def create_app():
    app = Flask(__name__)
    CORS(app)
    
    # Load configuration
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'postgresql://localhost/learning_db')
    app.config['REDIS_URL'] = os.getenv('REDIS_URL', 'redis://localhost:6379/0')
    
    # Register blueprints
    from app.routes import performance_bp, recommendations_bp, analytics_bp
    app.register_blueprint(performance_bp)
    app.register_blueprint(recommendations_bp)
    app.register_blueprint(analytics_bp)
    
    logger.info("Learning API Service initialized")
    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True, port=5000)
