from flask_wtf import FlaskForm
from wtforms import PasswordField, SubmitField, EmailField, IntegerField
from wtforms.validators import DataRequired


class TeacherForm(FlaskForm):
    email = EmailField("Электронная почта", validators=[DataRequired()])
    password = PasswordField("Пароль", validators=[DataRequired()])
    password_c = PasswordField("Повторите пароль", validators=[DataRequired()])
    safe_code = IntegerField("Введите код безопасности", validators=[DataRequired()])
    submit = SubmitField("Добавить")