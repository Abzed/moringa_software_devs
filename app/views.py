
from flask import render_template, url_for, flash, redirect, request
from app.main import db
from app.forms import WishlistForm
from app.models import Wishlist
from flask_login import login_user, current_user, logout_user, login_required

@app.route("/wishlist/new", methods=['GET', 'POST'])
@login_required
def new_wishlist():
    form = WishlistForm()
    if form.validate_on_submit():
        wishlist = Wishlist(content=form.content.data)
        db.session.add(wishlist)
        db.session.commit()
        flash('Added to your wishlist!', 'success')
        return redirect(url_for('wishlist'))
    return render_template('create_wishlist.html', title='New Wishlist',
                           form=form, legend='New Wishlist')


@app.route("/wishlist")
def wishlist():

    wishlist = Wishlist.query.all()
    return render_template('wishlist.html', wishlist=wishlist)