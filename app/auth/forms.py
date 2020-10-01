from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField,BooleanField,SelectField
from wtforms.validators import Required,Email,EqualTo
from ..models import User,Role,Department
from wtforms import ValidationError


class RegistrationForm(FlaskForm):
    staff = BooleanField('Staff')
    admin = BooleanField('Admin')
    email = StringField('User Email Address',validators=[Required(),Email()])
    username = StringField('Username',validators = [Required()])
    password = PasswordField('Password',validators = [Required(), EqualTo('password_confirm',message = 'Passwords must match')])
    password_confirm = PasswordField('Confirm Passwords',validators = [Required()])
    submit = SubmitField('Sign Up')
    
    def validate_email(self,data_field):
            if User.query.filter_by(email =data_field.data).first():
                raise ValidationError('There is an account with that email')

    def validate_username(self,data_field):
        if User.query.filter_by(username = data_field.data).first():
            raise ValidationError('That username is taken')
        
class LoginForm(FlaskForm):
    username = StringField('Enter Username',validators=[Required()])
    password = PasswordField('Password',validators =[Required()])
    remember = BooleanField('Remember me')
    submit = SubmitField('Log In')