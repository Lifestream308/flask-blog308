from datetime import datetime
# importing ma and bcrypt, check if this is ok
from flaskblog import db, login_manager, ma, bcrypt
from flask_login import UserMixin


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    # commenting out image file
    # image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    password = db.Column(db.String(60), nullable=False)
    posts = db.relationship('Post', backref='author', lazy=True)

# may be a problem with using __init__ because I don't want to show password here. I hash password elsewhere
    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = bcrypt.generate_password_hash(password).decode('utf-8')

    def __repr__(self):
        return f"User('{self.username}', '{self.email}')"
        # return f"User('{self.username}', '{self.email}', '{self.image_file}')"


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __init__(self, title, content):
        self.title = title
        self.content = content

    def __repr__(self):
        return f"Post('{self.title}', '{self.date_posted}')"



class UserSchema(ma.Schema):
    class Meta:
        fields = ['id', 'username', 'email']

user_schema = UserSchema()
users_schema = UserSchema(many=True)

class PostSchema(ma.Schema):
    class Meta:
        fields = ['id', 'title', 'content']

post_schema = PostSchema()
posts_schema = PostSchema(many=True)