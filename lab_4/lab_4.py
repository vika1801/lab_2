# lab_4.py

from flask import Flask, render_template_string, request, redirect, flash
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.secret_key = 'secret-key'

# Настройка базы данных
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login_get'

# Модель пользователя
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(200))
    name = db.Column(db.String(100))


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


# HTML
index_html = """
<h1>Лабораторная работа №4</h1>
<p>Аутентификация и авторизация</p>
<p>Вы вошли как: {{ current_user.name }}</p>
<a href="/logout">Выход</a>
"""

login_html = """
<h2>Вход</h2>
<form method="POST">
    Email: <input type="email" name="email" required><br>
    Password: <input type="password" name="password" required><br>
    <button type="submit">Войти</button>
</form>

<p style="color:red;">
{% for message in get_flashed_messages() %}
    {{ message }}
{% endfor %}
</p>

<a href="/signup">Регистрация</a>
"""

signup_html = """
<h2>Регистрация</h2>
<form method="POST">
    Name: <input type="text" name="name" required><br>
    Email: <input type="email" name="email" required><br>
    Password: <input type="password" name="password" required><br>
    <button type="submit">Зарегистрироваться</button>
</form>

<p style="color:red;">
{% for message in get_flashed_messages() %}
    {{ message }}
{% endfor %}
</p>

<a href="/login">Вход</a>
"""

@app.route('/')
def index():
    if current_user.is_authenticated:
        return render_template_string(index_html)
    return redirect('/login')


@app.route('/login', methods=['GET'])
def login_get():
    return render_template_string(login_html)


@app.route('/login', methods=['POST'])
def login_post():
    email = request.form.get('email')
    password = request.form.get('password')

    user = User.query.filter_by(email=email).first()

    if not user:
        flash('Пользователь не найден')
        return redirect('/login')

    if not check_password_hash(user.password, password):
        flash('Неверный пароль')
        return redirect('/login')

    login_user(user)
    return redirect('/')


@app.route('/signup', methods=['GET'])
def signup_get():
    return render_template_string(signup_html)


@app.route('/signup', methods=['POST'])
def signup_post():
    name = request.form.get('name')
    email = request.form.get('email')
    password = request.form.get('password')

    user = User.query.filter_by(email=email).first()

    if user:
        flash('Пользователь уже существует')
        return redirect('/signup')

    hashed_password = generate_password_hash(password)

    new_user = User(email=email, password=hashed_password, name=name)

    db.session.add(new_user)
    db.session.commit()

    return redirect('/login')


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect('/login')


# СОЗДАНИЕ БД
if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # создаёт файл users.db

    app.run(debug=True)