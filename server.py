from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import CSRFProtect
from forms.application import ApplicationFrom

app = Flask(__name__)

app.config["SECRET_KEY"] = "P++G!+=]cP8tuJ-T:a9sYZaDaD=H))"

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///User.sqlite3"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    surname = db.Column(db.String(100))
    email = db.Column(db.String(100))
    exams = db.Column(db.String(100))

    def __init__(self, name, surname, email, exams):
        self.name = name
        self.surname = surname
        self.email = email
        self.exams = exams


@app.route("/", methods=["GET"])
def index():
    return render_template("base.html")


@app.route("/application", methods=["GET", "POST"])
def application():
    form = ApplicationFrom()

    if form.validate_on_submit():
        name = form.name.data
        surname = form.surname.data
        email = form.email.data
        exams = form.exams.data

        new_application = User(name=name, surname=surname, email=email, exams=exams)

        db.session.add(new_application)

        db.session.commit()

        return render_template("base.html")

    return render_template("application.html", form=form)


if __name__ == '__main__':
    csrf = CSRFProtect(app)
    app.run(port=8080, host='127.0.0.1', debug=True)