def calculate_password_score(password):
    return (
        (len(password) > 12) * 2
        + any(char.isdigit() for char in password) * 2
        + any(char.isupper() for char in password) * 2
        + any(char.islower() for char in password) * 2
        + any(not char.isalnum() and not char.isspace for char in password) * 2
    )


def main():
    password = input("Введите пароль:")
    score = calculate_password_score(password)
    print(f"Рейтинг пароля: {score}")


if __name__ == "__main__":

    main()
