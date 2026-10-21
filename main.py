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