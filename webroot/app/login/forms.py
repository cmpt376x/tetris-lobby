from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, validators
from ..models import User


class LoginForm(FlaskForm):
    username = StringField('Username', [validators.DataRequired(), validators.Length(min=4, max=25)])
    password = PasswordField('Password', [validators.DataRequired()])
    submit = SubmitField('Log in')


class RegForm(FlaskForm):
    username = StringField('Username', [validators.DataRequired(), validators.Length(min=4, max=25)])
    password = PasswordField('Password', [validators.DataRequired(),
                                          validators.EqualTo('confirm', message='password must match')])
    confirm = PasswordField('Confirm password', [validators.DataRequired()])
    submit = SubmitField('Register')

    def validate_username(self, field):
        if User.query.filter_by(username=field.data).first():
            raise validators.ValidationError('Username already in use.')
