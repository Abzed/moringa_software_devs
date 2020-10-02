from flask import abort, render_template,flash,url_for,abort,request,redirect
from flask_login import current_user, login_required
from . import admin
from ..models import User,Role,Department,Post,Comment,Category
from .. import db,photos
from .forms import CategoryForm

# add admin dashboard view
@admin.route('/admin')
@login_required
def admin_dashboard():
    user = User.query.all()
    if not current_user.is_admin:
        abort(403)
    return render_template('admin.html', title="Admin Dashboard",user=user)

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

@admin.route('/category/new_category', methods=['GET','POST'])
@login_required
def new_category():
    user = User.query.all()
    category = Category.query.all()
    
    form = CategoryForm()
    if form.validate_on_submit():
        category = Category(name=form.category.data)
        
        Category.save_category(category)
        
        return redirect(url_for('admin.new_category', user=user,category=category))
    
    return render_template('new_category.html',user=user,form=form,category=category)

@admin.route('/categories/<int:id>')
def category(id):
    category = Category.query.get(id)
    blogs = Post.query.filter_by(categories=category.id).all()

    # pitches=Pitch.get_pitches(id)
    # title = f'{category.name} page'
    return render_template('category.html', blogs=blogs, category=category,id=id)


        
        
    
    
