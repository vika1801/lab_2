from flask import Flask, request, jsonify, render_template
import hashlib
import requests
from db import get_conn

app = Flask(__name__)


def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()


def get_user_by_id(user_id):
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("SELECT id, name FROM users WHERE id = %s", (user_id,))
    user = cur.fetchone()
    cur.close()
    conn.close()
    return user


def get_exchange_rate(currency):
    resp = requests.get(f"http://localhost:5001/rate?currency={currency}")

    if resp.status_code == 400:
        raise ValueError("Неизвестная валюта")

    if resp.status_code != 200:
        raise ValueError(f"Неожиданный ответ сервера: {resp.status_code}")

    data = resp.json()
    return data["rate"]


# Регистрация
@app.route("/reg", methods=["POST"])
def reg():
    data = request.get_json()

    if not data or "login" not in data or "password" not in data:
        return jsonify({"error": "Пожалуйста, введите логин и/или пароль"}), 400

    login = data["login"]
    password_hash = hash_password(data["password"])

    try:
        conn = get_conn()
        cur = conn.cursor()

        cur.execute("SELECT id FROM users WHERE name = %s", (login,))
        ex_user = cur.fetchone()

        if ex_user:
            cur.close() 
            conn.close()
            return jsonify({"error": "Такой пользователь уже существует"}), 400

        cur.execute(
            "INSERT INTO users (name, password_hash) VALUES (%s, %s)",
            (login, password_hash)
        )
        conn.commit()

        cur.close()
        conn.close()

        return jsonify({"message": "Успешно"}), 200

    except Exception as error:
        return jsonify({"error": str(error)}), 500


# Добавление операции
@app.route("/add_operation", methods=["POST"])
def add_operation():
    data = request.get_json()

    if not data:
        return jsonify({"error": "Пустой запрос"}), 400

    for field in ["user_id", "type_operation", "sum", "date"]:
        if field not in data:
            return jsonify({"error": f"Необходимо заполнить поле '{field}'"}), 400

    user_id = data["user_id"]
    type_operation = data["type_operation"]
    operation_sum = data["sum"]
    operation_date = data["date"]

    user = get_user_by_id(user_id)
    if user is None:
        return jsonify({"error": "Такой пользователь не найден"}), 404

    try:
        conn = get_conn()
        cur = conn.cursor()

        cur.execute(
            "INSERT INTO operations (date, sum, type_operation, user_id) VALUES (%s, %s, %s, %s)",
            (operation_date, operation_sum, type_operation, user_id)
        )
        conn.commit()

        cur.close()
        conn.close()

        return jsonify({"message": "ok"}), 200

    except Exception as error:
        return jsonify({"error": str(error)}), 500


# Просмотр операций
@app.route("/operations", methods=["GET"])
def get_operations():
    user_id = request.args.get("user_id")
    currency = request.args.get("currency", "RUB")

    if not user_id:
        return jsonify({"error": "user_id не может быть пустым!"}), 400

    if currency not in ("RUB", "USD", "EUR"):
        return jsonify({"error": "Валюта должна быть RUB, USD или EUR"}), 400

    user = get_user_by_id(int(user_id))
    if user is None:
        return jsonify({"error": "Такой пользователь не найден"}), 404

    exchange_rate = 1.0
    if currency != "RUB":
        try:
            exchange_rate = get_exchange_rate(currency)
        except Exception as error:
            return jsonify({"error": f"Не удалось получить курс валют: {error}"}), 500

    try:
        conn = get_conn()
        cur = conn.cursor()

        cur.execute(
            "SELECT id, date, sum, type_operation FROM operations WHERE user_id = %s",
            (user_id,)
        )
        rows = cur.fetchall()

        cur.close()
        conn.close()

        operations_list = []
        for row in rows:
            converted_sum = round(float(row[2]) / exchange_rate, 2)

            operations_list.append({
                "id": row[0],
                "date": str(row[1]),
                "sum": converted_sum,
                "currency": currency,
                "type_operation": row[3]
            })

        return jsonify({"operations": operations_list}), 200

    except Exception as error:
        return jsonify({"error": str(error)}), 500
    

#Страница операций
@app.route("/operations_page", methods=["GET"])
def operations_page():
    user_id = request.args.get("user_id")
    currency = request.args.get("currency", "RUB")
    message = request.args.get("message")

    if not user_id:
        return "user_id не указан", 400

    user = get_user_by_id(int(user_id))
    if user is None:
        return "Такой пользователь не найден", 404

    exchange_rate = 1.0
    if currency != "RUB":
        try:
            exchange_rate = get_exchange_rate(currency)
        except Exception as error:
            return "Не удалось получить курс валют: " + str(error), 500

    conn = get_conn()
    cur = conn.cursor()

    cur.execute(
        "SELECT id, date, sum, type_operation FROM operations WHERE user_id = %s",
        (user_id,)
    )
    rows = cur.fetchall()

    cur.close()
    conn.close()

    operations_list = []
    for row in rows:
        converted_sum = round(float(row[2]) / exchange_rate, 2)
        operations_list.append({
            "id": row[0],
            "date": str(row[1]),
            "sum": converted_sum,
            "type_operation": row[3]
        })

    return render_template(
        "operations.html",
        user_id=user_id,
        user_name=user[1],
        operations=operations_list,
        currency=currency,
        message=message
    )
if __name__ == "__main__":
    app.run(debug=True)
