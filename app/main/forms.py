from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import Required

class CommentForm(FlaskForm):
    title = StringField('Comment Title', validators=[Required()])
    comment = TextAreaField('Comments...')
    submit = SubmitField('submit')
    
class BioForm(FlaskForm):
    bio = TextAreaField('Write A Short Bio About You...')
    submit = SubmitField('Submit')

class CreateCategory(FlaskForm):
     category = StringField('Category', validators=[Required()])
     submit = SubmitField('Submit')

class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.', validators=[Required()])
    submit = SubmitField('Submit')
    
class BlogForm(FlaskForm):
    title = StringField('Article Title', validators=[Required()])
    blog = TextAreaField('Write Blog...')
    submit = SubmitField('submit')
