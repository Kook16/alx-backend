#!/usr/bin/env python3
'''Basic Flask app'''
from flask import Flask, render_template, request, g
from flask_babel import Babel, gettext

# Mock user data
users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}

# Create a Flask application instance
app = Flask(__name__)

# Initialize Flask-Babel for internationalization
babel = Babel(app)


class Config:
    '''Configuration class for Flask-Babel'''
    LANGUAGES = ["en", "fr"]  # Supported languages
    BABEL_DEFAULT_LOCALE = 'en'  # Default locale if none is specified
    BABEL_DEFAULT_TIMEZONE = 'UTC'  # Default timezone

# Load configuration from the Config class
app.config.from_object(Config)

def get_user() -> str:
    '''Retrieve the user from the mock
    user data based on the login_as parameter'''
    user_id = request.args.get('login_as')
    if user_id and user_id.isdigit() and int(user_id) in users:
        return users[int(user_id)]
    return None

@app.before_request
def before_request():
    '''Set the current user in the global context for each request'''
    g.user = get_user()

@babel.localeselector
def get_locale() -> str:
    '''Determine the locale to use based on URL
    parameters or accept languages'''
    # Check URL parameters for locale
    lang = request.args.get('locale')
    if lang in app.config['LANGUAGES']:
        return lang
    # Use the best match from the Accept-Language header
    # if no URL parameter is found
    return request.accept_languages.best_match(app.config['LANGUAGES'])

@app.route('/', strict_slashes=False)
def home() -> str:
    '''Render the home page template'''
    return render_template('5-index.html')


if __name__ == '__main__':
    # Run the application in debug mode
    app.run(debug=True)
