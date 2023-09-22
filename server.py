from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import CSRFProtect
from forms.application import ApplicationFrom

app = Flask(__name__)
app.config["SECRET_KEY"] = "P++G!+=]cP8tuJ-T:a9sYZaDaD=H))"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///Exam.sqlite3"

db = SQLAlchemy(app)


class Exam(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))

    def __init__(self, name):
        self.name = name


db.create_all()

db.Table(
    "examinitions",
    db.Column("exam_id", db.ForeignKey("exam.id"), primary_key=True)
)


@app.route("/", methods=["GET"])
def main():
    return render_template("base.html")


@app.route("/application", methods=["GET", "POST"])
def application():
    form = ApplicationFrom()
    return render_template("application.html", form=form)


if __name__ == '__main__':
    csrf = CSRFProtect(app)
    app.run(port=8080, host='127.0.0.1', debug=True)