PASSWORD = input("Введите пароль:")


def calculate_password_score(PASSWORD):
    special_symbols = "@#$%^&*()-_=+[]{}|;:',.<>/?!"
    return (
        (len(PASSWORD) > 12) * 2
        + any(char.isdigit() for char in PASSWORD) * 2
        + any(char.isupper() for char in PASSWORD) * 2
        + any(char.islower() for char in PASSWORD) * 2
        + any(char in special_symbols for char in PASSWORD) * 2
    )


print(f"Рейтинг пароля: {calculate_password_score(PASSWORD)}")
