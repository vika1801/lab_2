import requests
from flask import Flask, request, render_template

app = Flask(__name__)

# Адреса целевых микросервисов
CURRENCY_MANAGER_URL = "http://localhost:5001"
DATA_MANAGER_URL = "http://localhost:5002"

# Главная страница
@app.route("/")
def index():
    return render_template("index.html")

# Добавление валюты
@app.route("/load", methods=["POST"])
def load_currency():
    currency_name = request.form.get("currency_name")
    rate = request.form.get("rate")

    if not currency_name or not rate:
        return render_template("index.html", action="load", message="Заполните все поля")
    
    if float(rate) <= 0:
        return render_template("index.html", action="load", message="Курс должен быть больше 0")
    
    data = {
        "currency_name": currency_name,
        "rate": float(rate)
    }
    
    response = requests.post(f"{CURRENCY_MANAGER_URL}/load", json=data)
    message = response.json().get("message") or response.json().get("error")
    return render_template("index.html", action="load", message=message)

# Обновление курса валюты
@app.route("/update_currency", methods=["POST"])
def update_currency():
    currency_name = request.form.get("currency_name")
    rate = request.form.get("rate")

    if not currency_name or not rate:
        return render_template("index.html", action="update_currency", message="Заполните все поля")
    
    if float(rate) <= 0:
        return render_template("index.html", action="update_currency", message="Курс должен быть больше 0")

    data = {
        "currency_name": currency_name,
        "rate": float(rate)
    }
    response = requests.post(f"{CURRENCY_MANAGER_URL}/update_currency", json=data)
    message = response.json().get("message") or response.json().get("error")
    return render_template("index.html", action="update_currency", message=message)

# Удаление валюты
@app.route("/delete", methods=["POST"])
def delete_currency():
    currency_name = request.form.get("currency_name")

    if not currency_name:
        return render_template("index.html", action="delete", message="Заполните все поля")

    data = {
        "currency_name": currency_name
    }
    response = requests.post(f"{CURRENCY_MANAGER_URL}/delete", json=data)
    message = response.json().get("message") or response.json().get("error")
    return render_template("index.html", action="delete", message=message)

# Конвертация валюты
@app.route("/convert", methods=["GET"])
def convert():
    currency_name = request.args.get("currency_name")
    amount = request.args.get("amount")

    if not currency_name or not amount:
        return render_template("index.html", action="convert", result="Заполните все поля")

    if float(amount) <= 0:
        return render_template("index.html", action="convert", result="Сумма должна быть больше 0")
    
    params = {
        "currency_name": currency_name,
        "amount": float(amount)
    }
    response = requests.get(f"{DATA_MANAGER_URL}/convert", params=params)
    data = response.json()
    result = data.get("result") or data.get("error")
    return render_template("index.html", action="convert", result=result)

# Получение списка всех валют
@app.route("/currencies", methods=["GET"])
def currencies():
    response = requests.get(f"{DATA_MANAGER_URL}/currencies")
    currencies_list = response.json()
    return render_template("index.html", currencies_list=currencies_list)

if __name__ == "__main__":
    app.run(port=5000)
    