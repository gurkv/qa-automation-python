def check_age(age):
    if age >= 18:
        return ("совершеннолетний")
    else:
        return ("несовершеннолетний")

print(check_age(20))
print(check_age(17))
print(check_age(18))


def filter_even(numbers):
    result = []
    for num in numbers:
        if num % 2 == 0:
            result.append(num)
    return result

print(filter_even([5, 12, 8, 130, 44, 2]))

def get_user_info(user_dict):
    return f"Имя: {user_dict['name']}, Роль: {user_dict['role']}"


user = {"id": 101, "name": "Иван", "role": "admin", "is_active": True}
print(get_user_info(user))