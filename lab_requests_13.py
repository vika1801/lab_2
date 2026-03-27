from flask import Flask, request
import random

app = Flask(__name__)

# ПУНКТ 1 — GET
@app.route('/number/', methods=['GET'])
def get_number():
    param = int(request.args.get('param'))
    result = random.randint(1, 10) * param
    return {"number": result, "operation": "mul"}


# ПУНКТ 2 — POST
@app.route('/number/', methods=['POST'])
def post_number():
    data = request.get_json()
    param = int(data["jsonParam"])
    
    num = random.randint(1, 10)
    op = random.choice(["sum", "sub", "mul", "div"])
    
    if op == "sum":
        result = num + param
    elif op == "sub":
        result = num - param
    elif op == "mul":
        result = num * param
    else:
        result = num / param
    
    return {"number": result, "operation": op}


# ПУНКТ 3 — DELETE
@app.route('/number/', methods=['DELETE'])
def delete_number():
    return {
        "number": random.randint(1, 10),
        "operation": random.choice(["sum", "sub", "mul", "div"])
    }


if __name__ == "__main__":
    app.run(debug=True)