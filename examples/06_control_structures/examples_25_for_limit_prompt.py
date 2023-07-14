

for _ in range(5):
    num = input("Введіть число: ")
    if num.isdigit():
        print("Result", int(num) * 100)
        break
else:
    print("Спроби закінчились")
