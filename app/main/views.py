from flask import render_template,request,redirect,url_for,abort,flash
from . import main
from .forms import BioForm, CommentForm, UpdateProfile,BlogForm, MyForm
from ..models import User,Role,Department,Post,Comment
from ..models import User,Role,Department,Post,Comment,Category
from flask_login import login_required,current_user
from .. import db,photos
#from flask_user import roles_required

# @route() must always be the outer-most decorator
@main.route('/')
def index():
    user = User.query.all()  
    return render_template('index.html', user=user,posts=posts)

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

@main.route('/categories/view_pitch/add/<int:id>', methods=['GET','POST'])
@login_required
def new_blog(id):
    form = BlogForm()
    category = Category.query.filter_by(id=id).first()
    if form.validate_on_submit():
        post = form.post.data
        title = form.title.data
        new_post=Post(post=post,title=title,categories=category.id ,user_id=current_user.id)
        
        new_post.save_blog()
        
        return redirect(url_for('admin.category',id=category.id))
    
    return render_template('new_blog.html', form=form,legend='New Post',category = category)

@main.route('/all_posts', methods=['GET', 'POST'])
@login_required
def posts():
    posts = Post.query.all()
    
    return render_template('blogs.html',posts=posts)

@main.route('/categories/view_blog/<int:id>', methods=['GET', 'POST'])
@login_required
def view_pitch(id):
    '''
    Function the returns a single pitch for comment to be added
    '''
    blogs = Post.query.get(id)
    # pitches = P 2itch.query.filter_by(id=id).all()

    if blogs is None:
        abort(404)
    #
    #comment = Comments.get_comments(id)
    return render_template('category.html', blogs=blogs, category_id=id)

@app.route('/', methods=['GET', 'POST'])
def index():
    form = MyForm()

    if form.validate_on_submit():
        
        filename = images.save(form.image.data)
        return f'Filename: { filename }'

    return render_template('index.html', form=form)