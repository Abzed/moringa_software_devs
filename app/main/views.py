from flask import render_template,request,redirect,url_for,abort,flash
from . import main
from .forms import BioForm, CommentForm
from ..models import User,Role,Department,Post,Comment,Category
from flask_login import login_required,current_user
from .. import db,photos
#from flask_user import roles_required

# @route() must always be the outer-most decorator
@main.route('/')
def index():   
    user = User.query.all()  
    return render_template('home-page.html', user=user)

@main.route('/all_articles')
@login_required
def articles():
    category = Category.query.all()
    return render_template('articles.html',category=category)
