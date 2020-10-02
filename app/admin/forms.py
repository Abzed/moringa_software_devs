from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField,BooleanField,SelectField
from wtforms.validators import Required,Email,EqualTo
from ..models import User,Role,Department
from wtforms import ValidationError

class CategoryForm(FlaskForm):
    category = StringField('Add New Category',validators=[Required()])
    submit = SubmitField('Add')