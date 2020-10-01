from flask import abort, render_template
from flask_login import current_user, login_required
from . import admin

# add admin dashboard view
@admin.route('/admin')
def admin_dashboard():
 
    return render_template('admin.html', title="Admin Dashboard")