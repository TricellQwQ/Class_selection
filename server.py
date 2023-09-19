from flask import Flask, render_template
from flask_wtf.csrf import CSRFProtect
from forms.application import ApplicationFrom

app = Flask(__name__)
app.config['SECRET_KEY'] = "P++G!+=]cP8tuJ-T:a9sYZaDaD=H))"


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