import requests
import random

print("\n=== РАЗДЕЛ II ===\n")

# ПУНКТ 1 — GET
param = random.randint(1, 10)
print(f"GET /number/?param={param}")
g = requests.get(f"http://127.0.0.1:5000/number/?param={param}").json()
print(f"Ответ: {g}\n")

# ПУНКТ 2 — POST
json_param = random.randint(1, 10)
print(f"POST /number/ с jsonParam={json_param}")
p = requests.post(
    "http://127.0.0.1:5000/number/",
    json={"jsonParam": json_param}
).json()
print(f"Ответ: {p}\n")

# ПУНКТ 3 — DELETE
print("DELETE /number/")
d = requests.delete("http://127.0.0.1:5000/number/").json()
print(f"Ответ: {d}\n")

# ПУНКТ 4 — ВЫЧИСЛЕНИЕ
result = g["number"]

if p["operation"] == "sum":
    result += p["number"]
elif p["operation"] == "sub":
    result -= p["number"]
elif p["operation"] == "mul":
    result *= p["number"]
else:
    result /= p["number"]

if d["operation"] == "sum":
    result += d["number"]
elif d["operation"] == "sub":
    result -= d["number"]
elif d["operation"] == "mul":
    result *= d["number"]
else:
    result /= d["number"]

print(f"ИТОГ: {int(result)}")