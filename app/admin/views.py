from flask import abort, render_template
from flask_login import current_user, login_required
from . import admin

# add admin dashboard view
@admin.route('/admin')
@login_required
def admin_dashboard():
    if not current_user.is_admin:
        abort(403)
    return render_template('form.html', title="Admin Dashboard")