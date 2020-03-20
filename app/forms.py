from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms import StringField
from wtforms import TextAreaField
from wtforms import SelectField
from wtforms.validators import DataRequired
from wtforms.validators import Email

class ProfileForm(FlaskForm):
    firstName = StringField('Firstname',validators = [DataRequired()])
    lastName = StringField('Lastname',validators = [DataRequired()])
    gender = SelectField('Gender', choices = [('male','Male'),('female','Female')]) # to be written
    email = StringField('Email',validators = [DataRequired(),Email()])
    location = StringField('Location',validators = [DataRequired()])
    biography = TextAreaField('Biography', validators = [DataRequired()])
    profilePic = FileField('ProfilePic', validators = [FileRequired(),FileAllowed(['jpg','png','Images only!'])])

                           
