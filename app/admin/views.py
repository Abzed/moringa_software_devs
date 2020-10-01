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
    if not current_user.is_admin:
        abort(403)
    return render_template('form.html', title="Admin Dashboard",form=DeleteForm)

@admin.route('/users/delete/<int:id>', methods=['GET', 'POST'])
@login_required
def delete_user(id):
    """
    Deactivate a user from the database
    """
    user = User.query.all()
    user_mail = User.query.get(id)
    
    if not current_user.is_admin:
        abort(403)
        
    form = DeleteForm()
    if form.validate_on_submit:
        if form.email.data == user_mail.email:
            db.session.delete(user_mail)
            db.session.commit()
            
            flash('You have successfully deactivated the user.')
    
            # redirect to the home page    
            return redirect(url_for('admin.admin_dashboard',user=user,user_mail=user_mail,form=form))
        
    return render_template('delete.html')
        
        
    
    
