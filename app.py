from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_restx import Api
from config.user_config import DB_DSN
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql+psycopg2://{DB_DSN}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config["RESTX_VALIDATE"] = True
db = SQLAlchemy(app)
Base = db._make_declarative_base(model=db.Model)

migrate = Migrate(app, db)

from resources.auth import api as auth_api
from resources.registration import api as registration_api


api = Api(app, prefix="/api/v1/user", version="1.0", title="User Service API", description="User Service API")

api.add_namespace(auth_api)
api.add_namespace(registration_api)

