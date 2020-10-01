from flask import render_template,request,redirect,url_for,abort,flash
from . import main
from .forms import BioForm, CommentForm
from ..models import User,Role,Department,Post,Comment
from flask_login import login_required,current_user
from .. import db,photos
#from flask_user import roles_required

# @route() must always be the outer-most decorator
@main.route('/admin')
@login_required
def admin_dashboard():
    if not current_user.is_admin:
        abort(403)
    # render the admin dashboard
    return '<h1> Hi, Admin </h1>'

@main.route('/')
def index(): 
    
    return render_template('home-page.html')


