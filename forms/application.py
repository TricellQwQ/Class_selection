from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from wtforms_alchemy import QuerySelectMultipleField


class ApplicationFrom(FlaskForm):
    name = StringField("Имя", validators=[DataRequired()])
    surname = StringField("Фамилия", validators=[DataRequired()])
    exams = QuerySelectMultipleField("Экзамены", validators=[DataRequired()])
    submit = SubmitField("Отправить")