from flask import render_template,redirect,url_for,flash,request
from flask_login import login_user,logout_user,login_required,current_user
from ..models import User
from .forms import RegistrationForm, LoginForm
from .. import db
from . import auth
from ..email import mail_message

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for("main.index"))

@auth.route('/register',methods = ["GET","POST"])
@login_required
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(email = form.email.data, username = form.username.data,password = form.password.data,
                    is_admin =form.user_admin.data, is_staff=form.user_staff.data, is_student=form.user_student.data)
        
        db.session.add(user)
        db.session.commit()
        
        
        
        flash('Account Successfully created')
        
        return redirect(url_for('auth.login'))
        title = "New Account"
    return render_template('auth/register.html',registration_form = form)

@auth.route('/login',methods=['GET','POST'])
def login():
    login_form = LoginForm()
    if login_form.validate_on_submit():
        user = User.query.filter_by(username = login_form.username.data).first()
        if user is not None and user.verify_password(login_form.password.data):
            login_user(user,login_form.remember.data)
            if user.is_admin == True:
                return redirect( url_for('main.admin_dashboard'))
            elif user.is_staff == True:
                return redirect(url_for('main.staff_dashboard'))
            elif user.is_student == True:
                return redirect(url_for('main.student_dashboard'))

        flash('Invalid username or Password')

    title = " login"
    return render_template('auth/login.html',login_form = login_form,title=title)