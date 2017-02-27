"""
Sample flask web application.
"""

from flask import Flask, render_template

APP = Flask(__name__, static_url_path='/static')

@APP.route("/")
def hello():
    """
    Return Hello world string.
    """
    return "Hello World!"

@APP.route('/hello/')
@APP.route('/hello/<name>')
def hello_template(name=None):
    """
    Return Hello world from template.
    """
    return render_template('hello.html', name=name)

if __name__ == "__main__":
    APP.run()
