from flask_wtf import FlaskForm
from flask_wtf.file import FileAllowed, MultipleFileField
from wtforms import StringField, SubmitField, TextAreaField, URLField
from wtforms.validators import DataRequired, Length, Optional


class OpinionForm(FlaskForm):
    title = StringField(
        'Введите название фильма',
        validators=[
            DataRequired(message='Обязательное поле'),
            Length(min=1, max=128)
        ]
    )
    text = TextAreaField(
        'Напишите мнение',
        validators=[
            DataRequired(message='Обязательное поле')
        ]
    )
    source = URLField(
        'Добавьте ссылку на подробный обзор фильма',
        validators=[
            Optional(),
            Length(min=1, max=256)
        ]
    )
    images = MultipleFileField(
        validators=[
            FileAllowed(
                ['jpg', 'jpeg', 'png', 'gif', 'bmp'],
                message=(
                    'Выберите файлы с расширением '
                    '.jpg, .jpeg, .png, .gif или .bmp'
                )
            )
        ]
    )
    submit = SubmitField('Добавить')