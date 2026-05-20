from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config.from_object('settings')

db = SQLAlchemy(app)
migrate = Migrate(app, db)

from . import models, api_views, views, error_handlers, cli_commands  # noqa