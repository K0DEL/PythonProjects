import datetime
import requests
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    return render_template(
        "index.html", name="Keshav",
        year=datetime.datetime.now().year)


@app.route("/guess/<path:name>")
def search(name):
    age = requests.get(f"https://api.agify.io?name={name}").json()['age']
    gender = requests.get(
        f"https://api.genderize.io/?name={name}").json()['gender']

    return render_template(
        "guess.html", age=age, gender=gender, name=name
    )


@app.route("/blog/<num>")
def get_blog(num):
    print(num)
    blog_url = "https://api.npoint.io/5abcca6f4e39b4955965"
    response = requests.get(blog_url)
    all_posts = response.json()
    return render_template("blog.html", posts=all_posts)


if __name__ == "__main__":
    app.run(debug=True)
