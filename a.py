from flask import Flask, render_template, flash, request, redirect, url_for
from forms import LoginForm, RegistrationForm
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import check_password_hash, generate_password_hash

# create the object of Flask
app = Flask(__name__)

app.config['SECRET_KEY'] = 'hardsecretkey'

# SqlAlchemy Database Configuration With Mysql
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:''@localhost/flaskcodeloop'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


# This is our model
class UserInfo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))

    def __init__(self, username, password):
        self.username = username
        self.password = password


# creating our routes
@app.route('/')
def index():
    return render_template('index.html')


# login route
@app.route('/login', methods=['GET', 'POST'])
def Login():
    form = LoginForm()

    if form.validate_on_submit():
        if request.form['username'] != 'codeloop' or request.form['password'] != '12345':
            flash("Invalid Credentials, Please Try Again")


        else:
            return redirect(url_for('index'))

    return render_template('login.html', form=form)


# register route
@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()

    if form.validate_on_submit():
        hashed_password = generate_password_hash(form.password.data, method='sha256')
        username = form.username.data
        password = hashed_password

        new_register = UserInfo(username=username, password=password)

        db.session.add(new_register)

        db.session.commit()

        flash("Registration was successfull, please login")

        return redirect(url_for('Login'))

    return render_template('registration.html', form=form)


# run flask app
if __name__ == "__main__":
    app.run(debug=True)