from flask import Flask, render_template
import requests

response = requests.get("https://api.npoint.io/8f8ec29740c8bdfde7ee").json()
app = Flask(__name__)


@app.route('/')
def home():
    return render_template("index.html", blogs=response)


@app.route('/post/<int:id>')
def blog_post(id):
    return render_template("post.html", blog_data=response[id - 1])


if __name__ == "__main__":
    app.run(debug=True)
