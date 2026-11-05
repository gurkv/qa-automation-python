num = [5, 10, 15, 20, 25]
num_even = []
for i in num:
    print(i)
    if i % 2 == 0:
        num_even.append(i)
print(num_even)

user = {"id": 101, "name": "Иван", "role": "admin", "is_active": True}

for key, value in user.items():
    print (f"{key}:{value}")

print(user["name"])

users = [{"name": "Иван", "age": 30}, {"name": "Анна", "age": 17}, {"name": "Пётр", "age": 25}]

for user in users:
    print(user)

for user in users:
    if user['age'] >=18:
        print(f"{user['name']} совершеннолетний")
    else:
        print(f"{user['name']} несовершеннолетний")