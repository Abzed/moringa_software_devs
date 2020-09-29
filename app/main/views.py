from flask import render_template,request,redirect,url_for,abort,flash
from . import main
from .forms import BioForm, CommentForm
from ..model_admin import User
from flask_login import login_required,current_user
from .. import db,photos

@main.route('/')
def index():    
    return render_template('index.html')

