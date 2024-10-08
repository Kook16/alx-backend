#!/usr/bin/env python3
'''Basic Flask app'''
from flask import Flask, render_template
from flask_babel import Babel, _

app = Flask(__name__)


class Config:
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)
babel = Babel(app)


@babel.localeselector
def get_locale() -> str:
    return request.accept_languages.best_match(Config.LANGUAGES)


@app.route('/')
def home() -> str:
    '''A home route'''
    return render_template('index.html')


if __name__ == '__main__':
    app.run(host="0.0.0.0", port="5000")
