#!/usr/bin/env python3

"""
 a module to run 4-index.html web page
"""

from flask import Flask, render_template, request
from flask_babel import Babel

app = Flask(__name__)
babel = Babel(app)
""" instantiate the Babel object """


class Config(object):
    """
    config class
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)
""" Use that class as config for Flask app """


@app.route('/')
def index():
    """
    a function which renders 4-index.html file
    """
    return render_template('4-index.html')


@babel.localeselector
def get_locale():
    """to determine the best match with our supported languages"""
    local_language = request.args.get('locale')
    supported_languag = app.config['LANGUAGES']
    if local_language in supported_languag:
        return local_language
    else:
        return request.accept_languages.best_match(app.config['LANGUAGES'])


if __name__ == '__main__':
    app.run(debug=True)
