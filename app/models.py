from . import db, create_app
from werkzeug.security import generate_password_hash,check_password_hash 
from flask_login import UserMixin
from flask_security import RoleMixin
from . import login_manager
from datetime import datetime
from flask_security import SQLAlchemyUserDatastore, Security



class User(UserMixin,db.Model):
    __tablename__ = 'users'
    
    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(255),index=True)
    email = db.Column(db.String(255),unique = True,index = True)
    profile_pic_path = db.Column(db.String())
    pass_secure = db.Column(db.String(255))
    
    
    
    
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
    
#class Comment-id,commnt.... user_id.... post_id

#class Content..... DevOPs,Fullstack,Front-End

#Posts-Posts, title, category,id,user_id

#Likes-id, like..int

#Dislikes-id, like..int



    



    

