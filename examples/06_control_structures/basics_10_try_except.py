num1 = input("Введіть перше число: ")
num2 = input("Введіть друге число: ")

try:
    result = int(num1) / int(num2)
except ValueError as error:
    print("Щось пішло не так", error)
else:
    print("Результат", result)
finally:
    print("The end")
