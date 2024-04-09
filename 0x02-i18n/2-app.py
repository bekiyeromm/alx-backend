#!/usr/bin/env python3

"""
 a module to run 0-index.html web page
"""

from flask import Flask, render_template
from flask_babel import Babel

app = Flask(__name__)
babel = Babel(app)


class Config(object):
    """
    config class
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCAL = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)


@app.route('/')
def index():
    """
    a function which renders 0-index.html file
    """
    return render_template('2-index.html')


@babel.localeselector
def get_local():
    """to determine the best match with our supported languages"""
    return request.accept_languages.best_match(app.config['LANGUAGES'])


if __name__ == '__main__':
    app.run(debug=True)
