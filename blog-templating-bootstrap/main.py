from flask import Flask, render_template, request
import requests

response = requests.get("https://api.npoint.io/f591fd271b99580465a4").json()

app = Flask(__name__)


@app.route('/')
def home():
    return render_template("index.html", blogs=response)


@app.route('/about-us')
def about():
    return render_template('about.html')


@app.route("/contact-us", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        data = request.form
        print(data["name"])
        print(data["email"])
        print(data["phone"])
        print(data["message"])
        return render_template("contact.html", msg_sent=True)
    return render_template("contact.html", msg_sent=False)


@app.route('/post/<int:id>')
def post(id):
    return render_template('post.html', blog_data=response[id - 1])


if __name__ == "__main__":
    app.run(debug=True)
