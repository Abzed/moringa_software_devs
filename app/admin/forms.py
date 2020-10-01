from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField,BooleanField,SelectField
from wtforms.validators import Required,Email,EqualTo
from ..models import User,Role,Department
from wtforms import ValidationError

class DeleteForm(FlaskForm):
    email = StringField('User Email Address',validators=[Required(),Email()])
    submit = SubmitField('Deactivate')