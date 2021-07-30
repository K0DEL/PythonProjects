from flask import Flask

app = Flask(__name__)


def make_bold(function):
    def wrapper_function():
        str = function()
        return "<strong>" + str + "</strong>"

    return wrapper_function


@app.route("/")
@make_bold
def hello_world():
    return "<p>Hello, World!</p>"


if __name__ == '__main__':
    app.run(debug=True)
