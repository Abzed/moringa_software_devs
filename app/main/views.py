from flask import render_template,request,redirect,url_for,abort,flash
from . import main
# from ..request import get_quotes
from .forms import BlogForm,BioForm, CommentForm
from ..model_admin import User
from flask_login import login_required,current_user
from .. import db,photos
from ..request import get_quote
from werkzeug.contrib.atom import AtomFeed
from urllib.parse import urljoin

def get_abs_url(url):
    """ Returns absolute url by joining post url with base url """
    return urljoin(request.url_root, url)

@main.route('/')
@login_required
def index():
   
    return render_template('index.html')

@main.route('/feeds')
def feeds():
    feed = AtomFeed(title='Latest Posts from My Blog',
                    feed_url=request.url, url=request.url_root)

    # Sort post by created date
    a = A.query.all()

    for all in a:
        feed.add(all.title, all.posted,
                 content_type='html',
                 id = all.id,
                 author= all.blogger.username,
                 published=all.posted,
                 updated=all.posted)

    return feed.get_response()
