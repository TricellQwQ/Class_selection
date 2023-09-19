from flask_wtf import FlaskForm
from wtforms import StringField, RadioField, SubmitField
from wtforms.validators import DataRequired


class ApplicationFrom(FlaskForm):
    name = StringField("Имя", validators=[DataRequired()])
    surname = StringField("Фамилия", validators=[DataRequired()])
    exams = RadioField("Экзамены", choices=["Русский язык", "Математика", "Физика", "Химия", "Биология", "Литература", "География", "История", "Информатика", "Обществознание", "Английский язык", "Французский язык", "Немецкий язык", "Испанский язык"])
    submit = SubmitField("Отправить")