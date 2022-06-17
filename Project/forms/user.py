from flask_wtf import FlaskForm
from wtforms import (BooleanField, EmailField, PasswordField, StringField,
                     SubmitField)
from wtforms.validators import DataRequired


class RegisterForm(FlaskForm):
    nickname = StringField('Ник', validators=[DataRequired()])
    email = EmailField('Почта', validators=[DataRequired()])
    password = PasswordField('Пароль', validators=[DataRequired()])
    password_again = PasswordField(
        'Повторите пароль', validators=[DataRequired()])
    submit = SubmitField('Зарегистрироваться')


class UserChangeForm(FlaskForm):
    nickname = StringField('Ник')
    email = EmailField('Почта')
    password = PasswordField('Пароль')
    password_again = PasswordField(
        'Повторите пароль')
    submit = SubmitField('Сохранить')


class LoginForm(FlaskForm):
    nickname = StringField('Ник', validators=[DataRequired()])
    password = PasswordField('Пароль', validators=[DataRequired()])
    remember_me = BooleanField('Запомнить меня')
    submit = SubmitField('Войти')
