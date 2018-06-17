from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import InputRequired, Length,AnyOf


#AnyOf(values=['password','secret']

class LoginForm(FlaskForm):
    username = StringField('username', validators=[InputRequired('Please provide a Username'),Length(min=8,max=15,message='Too short or too long bro.')])
    password = PasswordField('password',validators=[InputRequired('Password required!')])