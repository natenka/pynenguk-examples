
username = input("Введіть ім'я користувача: ")
password = input("Введіть пароль: ")

numbers = set("0123456789")
correct_password = True

if len(password) < 8:
    print("Пароль надто короткий")
    correct_password = False
if username.lower() in password.lower():
    print("Пароль містить ім'я користувача")
    correct_password = False
if len(numbers.intersection(password)) < 3:
    print("У паролі мають бути хоча б три цифри")
    correct_password = False

if correct_password:
    print(f"Пароль для користувача {username} встановлено")

