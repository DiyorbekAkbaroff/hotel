from flask import (
    Flask,
    request,
    render_template,
    redirect,
    flash,
    url_for,
)
from db import DB
import config


app = Flask(__name__)
db = DB()

@app.route('/')
def home_view():
    return render_template('index.html')

@app.route('/about')
def about_view():
    return render_template('about.html')

@app.route('/contact')
def contact_view():
    return render_template('contact.html')

@app.route('/rooms')
def rooms_view():
    return render_template('rooms.html')

@app.route('/register')
def register_view():
    return render_template('register.html')

@app.route('/login')
def login_view():
    return render_template('login.html')


if __name__ == '__main__':
    app.run(
        host=config.HOST,
        port=config.PORT,
        debug=config.DEBUG
    )
