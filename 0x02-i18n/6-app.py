#!/usr/bin/env python3

"""
Basic Flask app, Basic Babel setup, Get locale from request,
Parametrize templates, Force locale with URL parameter, Mock logging in
Use user locale
"""

from flask import Flask, render_template, request, g
from flask_babel import Babel

app = Flask(__name__)
babel = Babel(app)
""" instantiate the Babel object """

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}
"""mocking user data"""


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
    a function which renders 6-index.html file
    """
    return render_template('6-index.html')


@babel.localeselector
def get_locale():
    """to determine the best match with our supported languages"""
    local_language = request.args.get('locale')
    supported_languag = app.config['LANGUAGES']
    if local_language in supported_languag:
        return local_language
    userId = request.args.get('login_as')
    if userId:
        local_language = users[int(userId)]['locale']
        if local_language in supported_languag:
            return local_language
    local_language = request.headers.get('locale')
    if local_language in supported_languag:
        return local_language
    return request.accept_languages.best_match(app.config['LANGUAGES'])


def get_user():
    """ returns a user dictionary or None
    if the ID cannot be found or if login_as was not passed """
    try:
        userId = request.args.get('login_as')
        return users[int(userId)]
    except Exception:
        return None


@app.before_request
def before_request():
    """ use get_user to find a user if any,
    and set it as a global on flask.g.user  """
    g.user = get_user()


if __name__ == '__main__':
    app.run(debug=True)