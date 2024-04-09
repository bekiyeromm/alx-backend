#!/usr/bin/env python3

"""
 a module to run 0-index.html web page
"""

from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def index():
    """
    a function which renders 0-index.html file
    """
    return render_template('0-index.html')


if __name__ == '__main__':
    app.run(debug=True)
