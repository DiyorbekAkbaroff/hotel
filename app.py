from flask import (
    Flask,
    request,
    render_template,
    redirect,
    flash,
    url_for,
    session
)
from db import DB
import config


app = Flask(__name__)
app.secret_key = config.SECRET_KEY

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
    rooms = db.get_rooms()
    return render_template('rooms.html', rooms=rooms)

@app.route('/rooms/<int:room_id>')
def room_detail_view(room_id):
    room = db.get_room(room_id)
    return render_template('room_detail.html', room=room)

@app.route('/register', methods=["GET", "POST"])
def register_view():
    if request.method == 'POST':
        created_user = db.create_user(
            name=request.form.get('name', ''),
            username=request.form.get('username', ''),
            email=request.form.get('email', ''),
            password=request.form.get('password', '')
        )
        if created_user:
            session['user'] = request.form['username']
            return redirect(url_for('login'))
        else:
            flash("Invalid information, Please check your information.")

    return render_template('register.html')

@app.route('/login', methods=["GET", "POST"])
def login_view():
    if request.method == 'POST':
        is_user = db.check_user(
            username=request.form.get('username', ''), 
            password=request.form.get('password', '')
        )
        if is_user:
            session['user'] = request.form['username']
            flash("You have logged in successfully.")
            return redirect(url_for("home_view"))
        else:
            flash("Invalid information, Please check your information.")

    return render_template('login.html')


if __name__ == '__main__':
    app.run(
        host=config.HOST,
        port=config.PORT,
        debug=config.DEBUG
    )
