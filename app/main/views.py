from flask import render_template,request,redirect,url_for,abort,flash
from . import main
from .forms import BioForm, CommentForm
from ..models import User,Role,Department,Post,Comment
from flask_login import login_required,current_user
from .. import db,photos
#from flask_user import roles_required

# @route() must always be the outer-most decorator
@main.route('/')
def index():   
    #user = User.query.all()  
    return render_template('index.html')

@main.route('/categories')
@login_required
def categories():
    return render_template('category-page.html')
