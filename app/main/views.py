from flask import render_template,request,redirect,url_for,abort,flash
from . import main
from .forms import BioForm, CommentForm
from ..models import User,Role,Department,Post,Comment,Upvote,Downvote
from flask_login import login_required,current_user
from .. import db,photos
from flask_user import roles_required

# @route() must always be the outer-most decorator
@main.route('/admin')
@roles_required('Admin')
def admin_dashboard():
    # render the admin dashboard
    return '<h1> Hi, Admin </h1>'

@main.route('/')
def index(): 
    roles = Role.query.all()   
    return render_template('index.html',roles=roles)


