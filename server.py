from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import CSRFProtect
from pandas import DataFrame
from forms.application import ApplicationForm
from forms.confirmation import ConfirmationForm
from forms.teacher import TeacherForm

app = Flask(__name__)

app.config["SECRET_KEY"] = "P++G!+=]cP8tuJ-T:a9sYZaDaD=H))"

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///user.sqlite3"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
safe_code = 9988776655


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    surname = db.Column(db.String(100))
    email = db.Column(db.String(100))
    exams = db.Column(db.String(500))
    points = db.Column(db.Integer)

    def __init__(self, name, surname, email, exams, points):
        self.name = name
        self.surname = surname
        self.email = email
        self.exams = ";".join(exams)
        self.points = points


class Teacher(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100))
    password = db.Column(db.String(100))

    def __init__(self, email, password):
        self.email = email
        self.password = password


with app.app_context():
    db.create_all()


def to_xlsx():
    students = [obj for obj in db.session.query(User)]
    df = DataFrame({
        "№": [i for i in range(1, len(students) + 1)],
        "Имя": [student.name for student in students],
        "Фамилия": [student.surname for student in students],
        "Почта": [student.email for student in students],
        "Баллы": [student.points for student in students]
    })
    df.to_excel("./excel/students.xlsx", sheet_name="Students", index=False)


@app.route("/", methods=["GET"])
def index():
    return render_template("base.html")


@app.route("/application", methods=["GET", "POST"])
def application():
    form = ApplicationForm()

    if form.validate_on_submit():
        name = form.name.data
        surname = form.surname.data
        email = form.email.data
        exams = form.exams.data

        if email in [obj[0] for obj in db.session.query(User.email)]:
            return render_template("application.html", form=form, message="Данная почта уже занята")

        points = 0
        for exam in exams:
            if exam in ["Физика", "Математика", "Информатика"]:
                points += 3

        new_application = User(name=name, surname=surname, email=email, exams=exams, points=points)

        db.session.add(new_application)

        db.session.commit()

        return render_template("base.html")

    return render_template("application.html", form=form, message="")


@app.route("/confirmation", methods=["GET", "POST"])
def confirmation():
    form = ConfirmationForm()

    if form.validate_on_submit():
        email = form.email.data
        password = form.password.data

        for teacher in db.session.query(Teacher).filter(Teacher.email==email):
            if teacher.email == email and teacher.password != password:
                return render_template("confirmation.html", form=form, message="Неверный пароль")
            else:
                to_xlsx()
                return render_template("base.html")
        return render_template("confirmation.html", form=form, message="Данная почта не зарегистрирована")

    return render_template("confirmation.html", form=form, message="")


@app.route("/teacher", methods=["GET", "POST"])
def teacher():
    form = TeacherForm()

    if form.validate_on_submit():
        email = form.email.data
        password = form.password.data
        password_c = form.password_c.data
        code = form.safe_code.data

        for teacher in [obj[0] for obj in db.session.query(Teacher.email)]:
            if teacher == email:
                return render_template("teacher.html", form=form, message="Почта занята")
        if password != password_c:
            return render_template("teacher.html", form=form, message="Пароли не совпадают")
        elif code != safe_code:
            return render_template("teacher.html", form=form, message="Неверный код безопасности")
        else:

            new_application = Teacher(email=email, password=password)

            db.session.add(new_application)

            db.session.commit()

            return render_template("base.html")
    return render_template("teacher.html", form=form, message="")


if __name__ == '__main__':
    csrf = CSRFProtect(app)
    app.run(port=8080, host='127.0.0.1', debug=True)