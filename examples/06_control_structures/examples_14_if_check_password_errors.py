
username = input("Введіть ім'я користувача: ")
password = input("Введіть пароль: ")

numbers = set("0123456789")
errors = ""

if len(password) < 8:
    errors += "Пароль надто короткий\n"
if username.lower() in password.lower():
    errors += "Пароль містить ім'я користувача\n"
if len(numbers.intersection(password)) < 3:
    errors += "У паролі мають бути хоча б три цифри\n"

if errors:
    print(errors)
else:
    print(f"Пароль для користувача {username} встановлено")


# if errors == ""
