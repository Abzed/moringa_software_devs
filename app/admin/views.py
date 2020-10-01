from flask import abort, render_template,flash,url_for,abort,request,redirect
from flask_login import current_user, login_required
from . import admin
from ..models import User,Role,Department,Post,Comment
from .. import db,photos
from .forms import DeleteForm

# add admin dashboard view
@admin.route('/admin')
@login_required
def admin_dashboard():
    user = User.query.all()
    if not current_user.is_admin:
        abort(403)
    return render_template('admin.html', title="Admin Dashboard",form=DeleteForm,user=user)

@admin.route('/users/delete/<int:id>', methods=['POST'])
@login_required
def delete_user(id):
    """
    Deactivate a user from the database
    """
    user = User.query.all()
    user_mail = User.query.get(id)
    
    if not current_user.is_admin:
        abort(403)
        
    db.session.delete(user_mail)
    db.session.commit()
                
    # redirect to the home page    
    return redirect(url_for('admin.admin_dashboard',user=user,user_mail=user_mail))
        
@admin.route('/admin/user_account_details')
@login_required
def all_users():
    user = User.query.all()
    
    return render_template('users.html',user=user)

        
        
    
    
