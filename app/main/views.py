from flask import render_template,request,redirect,url_for,abort,flash
from . import main
from .forms import BioForm, CommentForm, UpdateProfile,BlogForm
from ..models import User,Role,Department,Post,Comment
from ..models import User,Role,Department,Post,Comment,Category
from flask_login import login_required,current_user
from .. import db,photos
#from flask_user import roles_required

# @route() must always be the outer-most decorator
@main.route('/')
def index():   
    user = User.query.all()  
    return render_template('index.html', user=user)


@main.route('/all_articles')
@login_required
def categories():
    
    return render_template('blog.html')

@main.route('/staff/<uname>')
def profile(uname):
    user = User.query.filter_by(username = uname).first()

    if user is None:
        abort(404)

    return render_template("staff/profile.html", user = user)

@main.route('/staff/<uname>/update', methods=['GET', 'POST'])
@login_required
def update_profile(uname):
    user = User.query.filter_by(username=uname).first()
    if user is None :
        abort(404)

    form = UpdateProfile()

    if form.validate_on_submit():
        user.bio = form.bio.data

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile', uname=user.username))

    return render_template('staff/edit_bio.html', form=form)

@main.route('/staff/<uname>/update/pic',methods= ['POST'])
@login_required
def update_pic(uname):
    user = User.query.filter_by(username = uname).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path

        db.session.commit()

    return redirect(url_for('.profile',uname=uname))

@main.route('/all_articles')    
def articles():
    category = Category.query.all()
    return render_template('blogs.html',category=category)

@main.route('/new_blog', methods=['GET','POST'])
@login_required
def new_blog():
    form = BlogForm()
    if form.validate_on_submit():
        post = form.blog.data
        title = form.title.data
        new_blog=Post(post=post,title=title,user_id=current_user.id)
        
        new_blog.save_blog()
        
        return redirect(url_for('main.index'))
    
    return render_template('new_blog.html', form=form,legend='New Post')
