
num = ""

attempt = 1
while attempt <= 5 and not num.isdigit():
    print(attempt)
    num = input("Введіть число: ")
    attempt += 1

if num.isdigit():
    print("Result", int(num) * 100)
