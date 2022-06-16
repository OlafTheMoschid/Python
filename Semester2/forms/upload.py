from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FileField
from wtforms.validators import DataRequired


class UploadForm(FlaskForm):
    name = StringField('Название видео', validators=[DataRequired()])
    file_data = FileField('Файл', validators=[DataRequired()])
    submit = SubmitField('Добавить')


class VideoChangeForm(FlaskForm):
    name = StringField('Название видео')
    submit = SubmitField('Сохранить')
