from flask import Flask
from forms.application import ApplicationFrom

app = Flask(__name__)

@app.route("/", methods=["GET"])
def main():
    return "aboba"

@app.route("/application", methods=["GET", "POST"])
def application():
    form = ApplicationFrom()


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1', debug=True)