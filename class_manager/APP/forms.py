from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, TextAreaField, ValidationError, HiddenField, \
    BooleanField, PasswordField, IntegerField, DateTimeField, DateField
from wtforms.validators import DataRequired, Email, Length, Optional, URL, EqualTo


class LoginForm(FlaskForm):
    uid = StringField('ReaderID', validators=[DataRequired(), Length(1, 20)])
    password = PasswordField('Password', validators=[DataRequired(), Length(6, 20)])
    remember = BooleanField('Remember me')
    submit = SubmitField('Log in')


class RegisterForm(FlaskForm):
    RID = StringField('RID', validators=[DataRequired(), Length(1, 20)])
    rName = StringField('readerName', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired(),
                                                     Length(1, 20),
                                                     EqualTo('password_confirm', message='password doesn`t match')])
    password_confirm = PasswordField('Password_confirm', validators=[DataRequired()])
    department = StringField('Department', validators=[DataRequired(), Length(1, 20)])
    major = StringField('Department', validators=[DataRequired(), Length(1, 20)])
    submit = SubmitField('Register')
