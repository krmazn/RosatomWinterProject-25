import os

def get_token():
    """Читает Telegram API токен из файла."""
    token_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "token.txt")

    try:
        with open(token_path, "r") as file:
            token = file.read().strip()
            if not token:
                raise ValueError("Токен пустой.")
            return token
    except FileNotFoundError:
        raise FileNotFoundError("Файл token.txt не найден. Проверьте путь к файлу с токеном.")

get_token()