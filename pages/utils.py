import secrets
import string
import time


def generate_password(self, length=12):
    # Проверяем, что длина не менее 9
    if length < 9:
        length = 9
    # Определяем наборы символов
    letters_low = string.ascii_lowercase
    letters_up = string.ascii_uppercase
    digits = string.digits
    # Исключаем @ из спецсимволов
    special_chars = string.punctuation.replace("@", "")
    # Объединяем все разрешенные символы
    all_chars = letters_low + letters_up + digits + special_chars
    while True:
        # Генерируем пароль заданной длины
        password = ''.join(secrets.choice(all_chars) for _ in range(length))
        # Проверяем выполнение всех условий сложности (минимум по 1 символу каждого типа)
        if (any(c in letters_low for c in password) and
                any(c in letters_up for c in password) and
                any(c in digits for c in password) and
                any(c in special_chars for c in password)):
            return password

def generate_email(self):
    # Создаем новый email
    email = str(time.time()) + "@fakemail.org"
    return email
