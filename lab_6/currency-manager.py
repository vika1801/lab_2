from flask import Flask, request, jsonify
import psycopg2

app = Flask(__name__)


def get_connection():
    connection = psycopg2.connect(
        host="localhost",
        database="lab_6",
        user="postgres",
        password="postgres"
    )

    return connection


@app.route('/load', methods=['POST'])
def load_currency():
    data = request.json

    currency_name = data['currency_name']
    rate = data['rate']

    connection = get_connection()
    cursor = connection.cursor()

    # Проверка существования валюты
    cursor.execute(
        "SELECT * FROM currencies WHERE currency_name = %s",
        (currency_name,)
    )

    currency = cursor.fetchone()

    if currency:
        cursor.close()
        connection.close()

        return jsonify({
            "message": "Валюта уже существует"
        }), 409

    # Добавление валюты
    cursor.execute(
        """
        INSERT INTO currencies (currency_name, rate)
        VALUES (%s, %s)
        """,
        (currency_name, rate)
    )

    connection.commit()

    cursor.close()
    connection.close()

    return jsonify({
        "message": "Валюта добавлена"
    }), 200


@app.route('/update_currency', methods=['POST'])
def update_currency():
    data = request.json

    currency_name = data['currency_name']
    rate = data['rate']

    connection = get_connection()
    cursor = connection.cursor()

    # Проверка существования валюты
    cursor.execute(
        """
        SELECT * FROM currencies
        WHERE currency_name = %s
        """,
        (currency_name,)
    )

    currency = cursor.fetchone()

    if not currency:
        cursor.close()
        connection.close()

        return jsonify({
            "message": "Валюта не найдена"
        }), 404

    # Обновление курса
    cursor.execute(
        """
        UPDATE currencies
        SET rate = %s
        WHERE currency_name = %s
        """,
        (rate, currency_name)
    )

    connection.commit()

    cursor.close()
    connection.close()

    return jsonify({
        "message": "Курс обновлен"
    }), 200


@app.route('/delete', methods=['POST'])
def delete_currency():
    data = request.json

    currency_name = data['currency_name']

    connection = get_connection()
    cursor = connection.cursor()

    # Проверка существования валюты
    cursor.execute(
        """
        SELECT * FROM currencies
        WHERE currency_name = %s
        """,
        (currency_name,)
    )

    currency = cursor.fetchone()

    if not currency:
        cursor.close()
        connection.close()

        return jsonify({
            "message": "Валюта не найдена"
        }), 404

    # Удаление валюты
    cursor.execute(
        """
        DELETE FROM currencies
        WHERE currency_name = %s
        """,
        (currency_name,)
    )

    connection.commit()

    cursor.close()
    connection.close()

    return jsonify({
        "message": "Валюта удалена"
    }), 200


if __name__ == '__main__':
    app.run(port=5001)