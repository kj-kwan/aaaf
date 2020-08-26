# aaaf/__init__.py
import os
from flask import Flask, Blueprint
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from sqlalchemy import create_engine

app = Flask(__name__)

app.config['SECRET_KEY'] = 'SECRET_KEY'

basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+os.path.join(basedir,'data.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['UPLOAD_FOLDER'] = os.path.join(basedir,'static/imgs')

db = SQLAlchemy(app)
Migrate(app,db)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'users.login'

from .core.views import core
from .users.views import users
from .blogs.views import blog_posts
from .error_pages.handlers import error_pages

admin = Blueprint('admin', __name__,
    template_folder='templates',
    static_folder='static',
    static_url_path='/static')

app.register_blueprint(admin)
app.register_blueprint(core)
app.register_blueprint(users)
app.register_blueprint(blog_posts)
app.register_blueprint(error_pages)
# app.register_blueprint(news)
