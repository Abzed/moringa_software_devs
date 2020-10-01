from . import db, create_app, LoginManager
from werkzeug.security import generate_password_hash,check_password_hash 
from flask_login import UserMixin, current_user
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
    pass_secure = db.Column(db.String(255))
    is_admin = db.Column(db.Boolean, default=False)
    is_staff = db.Column(db.Boolean, default=False)
    role_id = db.Column(db.Integer, db.ForeignKey('role.id'))
    department_id = db.Column(db.Integer, db.ForeignKey('departments.id'))    
    
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
    name = db.Column(db.String(50))
    description = db.Column(db.String(200))
    user_id = db.relationship('User', backref='roles', lazy='dynamic')
    
class Department(db.Model):
    __tablename__ = 'departments'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(60), unique=True)
    description = db.Column(db.String(200))
    userss = db.relationship('User', backref='department', lazy='dynamic')

    def __repr__(self):
        return '<Department: {}>'.format(self.name)
    
class Post(db.Model):
    __tablename__ = 'posts'
    
    id = db.Column(db.Integer,primary_key=True)
    title = db.Column(db.String(255),nullable=False)
    post = db.Column(db.String(255),nullable=False)
    category = db.Column(db.String(255), index = True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    posted = db.Column(db.DateTime,default=datetime.utcnow,onupdate=datetime.utcnow())
    
    def save_blog(self):
        db.session.add(self)
        db.session.commit()
        
    def delete(self):
        db.session.delete(self)
        db.session.commit()
        
    @classmethod
    def get_blog(cls,id):
        posts = Post.query.filter_by(user_id=id).all()
        return posts

    
class Comment(db.Model):
    __tablename__ = 'comments' 
    
    id = db.Column(db.Integer, primary_key = True)
    comments = db.Column(db.Text(),nullable=False)
    title = db.Column(db.String(),nullable=False)
    post_id = db.Column(db.Integer,db.ForeignKey('posts.id'))
    user_id = db.Column(db.Integer,db.ForeignKey('users.id'))
    
    def save_comment(self):
        db.session.add(self)
        db.session.commit()
        
    def delete_comment(self):
        db.session.delete(self)
        db.session.commit()
        
    @classmethod
    def get_comments(cls,blog_id):
        comments = Comment.query.filter_by(post_id=post_id).all()

        return comments
        
    def __repr__(self):
        return f'Comment{self.comments}'
    

    
#class Comment-id,commnt.... user_id.... post_id

#class Content..... DevOPs,Fullstack,Front-End

#Posts-Posts, title, category,id,user_id

#Likes-id, like..int

#Dislikes-id, like..int



    



    

