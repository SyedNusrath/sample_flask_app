"""
    app.py
    ~~~~~~
    This simple sample application provides a bare-bones website that allows
    you to:
    - Create new user accounts.
    - Log into existing user accounts.
    - View a simple dashboard page that displays user information.
    - Edit your user information on said dashboard page.
    - Log out of the website.
    Please see the README for more information of how to run and use this
    sample application.
"""


from os import environ

from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)

##### Website
@app.route('/')
def index():
    """Basic home page."""
    return render_template('index.html')
	

if __name__ == '__main__':
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.run(port=5002, use_reloader=True)