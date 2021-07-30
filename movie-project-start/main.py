from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FloatField
from wtforms.validators import InputRequired
import requests
import os

FILE_URI = "sqlite:///movies_collection.db"
API_KEY = "376a1988b7ca103262cb1a5199c07f5c"
MOVIE_URL = "https://api.themoviedb.org/3/search/movie?"
SEARCH_URL = "https://api.themoviedb.org/3/movie/"

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap(app)

app.config['SQLALCHEMY_DATABASE_URI'] = FILE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Create Form


class EditForm(FlaskForm):
    rating = FloatField(label='Rating', validators=[InputRequired()])
    review = StringField(label='Review', validators=[InputRequired()])
    submit = SubmitField(label='Done')


class AddForm(FlaskForm):
    name = StringField(label='Movie Name', validators=[InputRequired()])
    submit = SubmitField(label='Done')

# Create Table


class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    year = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String, nullable=False)
    rating = db.Column(db.Float, nullable=False)
    ranking = db.Column(db.Integer, nullable=False)
    review = db.Column(db.String, nullable=False)
    img_url = db.Column(db.String, nullable=False)

    def __repr__(self):
        return f'<Movie {self.title}>'


if not os.path.isfile(FILE_URI):
    db.create_all()

# Add Movies
# new_movie = Movie(
#     title="Phone Booth",
#     year=2002,
#     description="Publicist Stuart Shepard finds himself trapped in a phone booth, pinned down by an extortionist's sniper rifle. Unable to leave or receive outside help, Stuart's negotiation with the caller leads to a jaw-dropping climax.",  # noqa E501
#     rating=7.3,
#     ranking=10,
#     review="My favourite character was the caller.",
#     img_url="https://image.tmdb.org/t/p/w500/tjrX2oWRCM3Tvarz38zlZM7Uc10.jpg"
# )
# db.session.add(new_movie)
# db.session.commit()

# Read Movies


@app.route("/")
def home():
    # all_movies = db.session.query(Movie).all()
    # all_movies = sorted(all_movies, key=lambda i: i.rating, reverse=True)
    # This is similar to the above statement
    all_movies = Movie.query.order_by(Movie.rating).all()
    for i in range(0, len(all_movies)):
        all_movies[i].ranking = i+1
    return render_template("index.html", movies=all_movies)


@app.route('/edit', methods=['GET', 'POST'])
def edit():
    edit_form = EditForm()
    if request.method == 'POST':
        if edit_form.validate_on_submit():
            movie_id = request.args.get('id')
            movie = Movie.query.get(movie_id)
            movie.rating = edit_form.rating.data
            movie.review = edit_form.review.data
            db.session.commit()
            return redirect(url_for('home'))
    return render_template('edit.html', form=edit_form)


@app.route('/delete', methods=['GET', 'POST'])
def delete():
    movie_id = request.args.get('id')
    movie = Movie.query.get(movie_id)
    db.session.delete(movie)
    db.session.commit()
    return redirect(url_for('home'))


@app.route('/add', methods=['GET', 'POST'])
def add():
    add_form = AddForm()
    if request.method == 'POST':
        movie_name = add_form.name.data
        params = {
            "api_key": API_KEY,
            "query": movie_name,
        }
        movies = requests.get(url=MOVIE_URL, params=params).json()['results']
        print('movies')
        return render_template('select.html', movie_list=movies)
    return render_template('add.html', form=add_form)


@app.route('/find')
def find():
    search_id = request.args.get('search_id')
    print(search_id)
    params = {
        "api_key": API_KEY,
    }
    movie_details = requests.get(
        url=SEARCH_URL+search_id+"?", params=params).json()
    print(movie_details)
    new_movie = Movie(
            title=movie_details['original_title'],
            year=int(movie_details['release_date'].split("-")[0]),
            description=movie_details['overview'],  # noqa E501
            rating=0,
            ranking=0,
            review="",
            img_url=("https://image.tmdb.org/t/p/w500" + \
                     movie_details['poster_path'])
        )
    db.session.add(new_movie)
    db.session.commit()
    return redirect(url_for('edit', id=new_movie.id))


if __name__ == '__main__':
    app.run(debug=True)
