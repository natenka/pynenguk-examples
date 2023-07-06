
username = input("Введіть ім'я користувача: ")
password = input("Введіть пароль: ")

numbers = set("0123456789")

if len(password) < 8:
    print("Пароль надто короткий")
elif username.lower() in password.lower():
    print("Пароль містить ім'я користувача")
elif len(numbers.intersection(password)) < 3:
    print("У паролі мають бути хоча б три цифри")
else:
    print(f"Пароль для користувача {username} встановлено")


password = "123test456"

counter = 0
for sym in password:
    if sym.isdigit():
        counter += 1

password = "123test456"

for sym in password:
    if sym.isdigit():
        print(sym)


count_int = set()

for sym in password:
    if sym.isdigit():
        count_int.add(sym)


count_int
{'1', '2', '3', '4', '5', '6'}

password = "123test123"

count_int = set()

for sym in password:
    if sym.isdigit():
        count_int.add(sym)

password = "123test123"
print(set(password) & set("0123456789"))

