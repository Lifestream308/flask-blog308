from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__)

app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'
# commenting out original elephant sql database so I can use Heroku's database
# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://dixzhcpa:P3IGf0VEANwR4uG1FO-VAaBHZ8MUKR7s@heffalump.db.elephantsql.com/dixzhcpa'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://zfarqkcstxzwbb:753cc730dcb60bdf7d6f7ca62b1bf694d86a9a023c1b1588fbde3e435d64271e@ec2-3-223-242-224.compute-1.amazonaws.com:5432/d60vpf3tooiq23'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'

from flaskblog import routes

# To create Database go into Python, >>>from flaskblog import db           >>>db.create_all()     
# >>>from flaskblog import User, Post       >>>user_1 = User(username='Corey', email='C@demo.com', password='password')     >>>db.session.add(user_1)       >>>db.session.commit()     >>>User.query.all()   >>>user=User.query.first()   >>>user.id    >>>user.email    >>>user.username