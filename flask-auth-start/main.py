from flask import Flask, render_template, request, url_for, redirect, flash, send_from_directory  # noqa 501
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import exc
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user  # noqa 501

app = Flask(__name__)

app.config['SECRET_KEY'] = 'any-secret-key-you-choose'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


login_manager = LoginManager()
login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# CREATE TABLE IN DB


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))
# Line below only required once, when creating DB.
# db.create_all()


@app.route('/')
def home():
    print(current_user.is_authenticated)
    return render_template("index.html",
                           logged_in=current_user.is_authenticated)


@app.route('/register', methods=['GET', 'POST'])
def register():
    error = None
    if request.method == 'POST':
        new_user = User(
            name=request.form['name'],
            email=request.form['email'],
            password=generate_password_hash(
                request.form['password'],
                method='pbkdf2:sha256',
                salt_length=8),
        )
        try:
            db.session.add(new_user)
            db.session.commit()
        except exc.IntegrityError:
            db.session.rollback()
            error = "email already exist"

        # Log in and authenticate user after adding details to database.
        else:
            login_user(new_user)
            return redirect(url_for('secrets'))

    return render_template("register.html", error=error,
                           logged_in=current_user.is_authenticated)


@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        user = db.session.query(User).filter_by(email=email).first()

        if user is None:
            error = "This email does not exist in the database"

        else:
            if check_password_hash(user.password, password):
                login_user(user)
                return redirect(url_for('secrets'))
            else:
                error = "Incorrect Password Entered"

    return render_template("login.html", error=error,
                           logged_in=current_user.is_authenticated)


@app.route('/secrets')
@login_required
def secrets():
    print(current_user.name)
    return render_template("secrets.html", name=current_user.name,
                           logged_in=True)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home'))


@app.route('/download')
@login_required
def download():
    return send_from_directory(
        directory="static/files",
        path="cheat_sheet.pdf",
        as_attachment=False
    )


if __name__ == "__main__":
    app.run(debug=True)
