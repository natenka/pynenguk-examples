
num = ""

attempt = 1
while not num.isdigit():
    if attempt > 5:
        print("Спроби закінчились")
        break
    num = input("Введіть число: ")
    attempt += 1
else:
    print("Result", int(num) * 100)
