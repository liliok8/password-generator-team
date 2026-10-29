import random
import string

def generate_password(length=12):
    """Функція №1: Генерація набору символів для пароля"""
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

if __name__ == "__main__":
    print("--- Тестування функції генерації пароля ---")
    my_pass = generate_password()
    print("Згенерований пароль:", my_pass)

def check_strength(password):
    """Функція №2: Перевірка складності пароля"""
    if len(password) < 8:
        return "Слабкий пароль (менше 8 символів)"
has_digit = any(char.isdigit() for char in password)
has_upper = any(char.isupper() for char in password)

if has_digit and has_upper:
    return "Сильний пароль!"
return "Середній пароль"