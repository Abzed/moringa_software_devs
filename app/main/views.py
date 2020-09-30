from flask import render_template,request,redirect,url_for,abort,flash
from . import main
from .forms import BioForm, CommentForm
from ..models import User,Role,UserRoles
from flask_login import login_required,current_user
from .. import db,photos
from flask_user import roles_required

# @route() must always be the outer-most decorator
@main.route('/admin/dashboard')
@roles_required('Admin')
def admin_dashboard():
    # render the admin dashboard
    return render_template('admin.html')

@main.route('/')
def index():    
    return render_template('index.html')
