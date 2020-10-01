from flask import render_template,request,redirect,url_for,abort,flash
from . import main
from .forms import BioForm, CommentForm
from ..models import User
from flask_login import login_required,current_user
from .. import db,photos
from flask_user import roles_required

# @route() must always be the outer-most decorator
@main.route('/admin/dashboard')
@login_required
def admin_dashboard():
    # render the admin dashboard
    return render_template('profile_admin/admin.html')

@main.route('/student/dashboard')
@login_required
def student_dashboard():
    # render the admin dashboard
    return render_template('student/student_dashboard.html')


@main.route('/student/profile')
@login_required
def student_profile():
    # render the admin dashboard
    return render_template('student/profile.html')


@main.route('/staff/courses')
@login_required
def staff_dashboard():
    # render the admin dashboard
    return render_template('staff/staff_dashboard.html')

@main.route('/staff/profile')
@login_required
def staff_profile():
    # render the admin dashboard
    return render_template('staff/profile.html')

@main.route('/')
def index():    
    return render_template('index.html')

@main.route('/courses')
@login_required
def courses():
    # render the admin dashboard
    return render_template('content.html')
