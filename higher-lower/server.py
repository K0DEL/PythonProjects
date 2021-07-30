from flask import Flask
import random

answer = random.randint(0, 9)


app = Flask(__name__)


@app.route("/")
def home_page():
    return "<h1>Guess The Number between 0 and 9</h1>"\
        "<img src='https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/"\
        "giphy.gif'></img>"


@app.route("/<int:number>")
def number_page(number):
    if number == answer:
        return "<h1 style='color:green;'> You got the right answer!</h1>"\
            "<img src='https://media.giphy.com/media/4T7e4DmcrP9du/"\
            "giphy.gif'></img>"
    elif number < answer:
        return "<h1 style='color:red;'> Your guess is too low</h1>"\
            "<img src='https://media.giphy.com/media/jD4DwBtqPXRXa/"\
            "giphy.gif'></img>"
    else:
        return "<h1 style='color:blue;'> Your guess is too high</h1>"\
            "<img src='https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/"\
            "giphy.gif'></img>"


if __name__ == '__main__':
    app.run(debug=True)
