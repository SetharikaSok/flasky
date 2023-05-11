from flask import Flask
#import SQLAlchemy
from flask_sqlalchemy import SQLAlchemy
#import Migrate
from flask_migrate import Migrate
#import library for grabing environtment varieables
from dotenv import load_dotenv
#use to read environtment variables
import os

#give us accese to operation
db = SQLAlchemy()
migrate = Migrate()
#load the value from our .env file so the os module to be able to see them
load_dotenv()

def create_app(test_config = None):
    app = Flask(__name__)

    #set up the database
    if not test_config:
        #dev environtment configuration
        app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
        # app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get ("SQLALCHEMY_DATABASE_URI")
        app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get ("RENDER_DATABASE_URI")
    else:
        #test environtment configuration
        #if there is a test_config passed in,
        #this means we're trying to test the app,
        #configure the test settings
        app.config["TESTING"] = True
        app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
        app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get("SQLALCHEMY_TEST_DATABASE_URI")
    

    db.init_app(app)
    migrate.init_app(app,db)

    #import route
    from .routes import crystal_bp, healer_bp

    #register blueprint
    app.register_blueprint(crystal_bp)
    app.register_blueprint(healer_bp)

    from app.models.crystal import Crystal
    from app.models.healer import Healer

    return app