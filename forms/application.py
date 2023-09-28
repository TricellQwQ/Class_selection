from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectMultipleField, EmailField, widgets
from wtforms.validators import DataRequired


class SelectMultipleFieldWithCheckboxes(SelectMultipleField):
    widget = widgets.ListWidget(prefix_label=False)
    option_widget = widgets.CheckboxInput()


class ApplicationFrom(FlaskForm):
    name = StringField("Имя", validators=[DataRequired()])
    surname = StringField('Фамилия', validators=[DataRequired()])
    email = EmailField("Электронная почта", validators=[DataRequired()])
    exams = SelectMultipleFieldWithCheckboxes("Экзамены", choices=["Русский язык", "Математика", "Физика", "Химия",
                                                                   "Биология", "Литература", "География", "История",
                                                                   "Информатика", "Обществознание", "Английский язык",
                                                                   "Французский язык", "Немецкий язык",
                                                                   "Испанский язык"])

    submit = SubmitField('Отправить')
