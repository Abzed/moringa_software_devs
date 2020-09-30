from . import db
from werkzeug.security import generate_password_hash,check_password_hash 
from flask_login import UserMixin
from flask_security import RoleMixin
from . import login_manager
from datetime import datetime

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(UserMixin,db.Model):
    __tablename__ = 'users'
    
    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(255),index=True)
    email = db.Column(db.String(255),unique = True,index = True)
    profile_pic_path = db.Column(db.String())
    pass_secure = db.Column(db.String(255))
    roles = db.relationship('Role', secondary='user_roles', backref='uname', lazy='dynamic' )
    active = db.Column(db.Boolean())
    
    
    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')
    
    @password.setter
    def password(self,password):
        self.pass_secure = generate_password_hash(password)
        
    def verify_password(self,password):
        return check_password_hash(self.pass_secure,password)
    
    def __repr__(self):
        return f'User {self.username}'
    
class Role(db.Model, RoleMixin):
    
    __tablename__ = 'role'
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(50), unique=True)

# Define the UserRoles association table        
class UserRoles(db.Model):
    __tablename__ = 'user_roles'
    id = db.Column(db.Integer(), primary_key=True)
    user_id = db.Column(db.Integer(), db.ForeignKey('users.id'))
    role_id = db.Column(db.Integer(), db.ForeignKey('role.id'))


    

