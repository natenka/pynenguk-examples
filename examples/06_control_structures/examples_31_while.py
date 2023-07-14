
num = ""

# while num.isdigit() == False:
while not num.isdigit():
    num = input("Введіть число: ")

print("Result", int(num) * 100)
