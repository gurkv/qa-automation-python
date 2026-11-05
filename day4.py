import json

def safe_divide(a, b):
    try:
        return a/b
    except ZeroDivisionError:
        return "Ошибка: деление на ноль"

print(safe_divide(10, 2))
print(safe_divide(10, 0))

def to_number(text):
    try:
        return int(text)
    except ValueError:
        return "Это не число"

print(to_number("123"))
print(to_number("abc"))


json_string = '{"id": 101, "status": "ok", "message": "User created"}'

data = json.loads(json_string)
print (data["status"])