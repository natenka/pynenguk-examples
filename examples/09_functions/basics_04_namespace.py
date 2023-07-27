from pprint import pprint

num1 = 10
num2 = 20

print(f"{num1=} {num2=}")

def sum_numbers(num1, num2):
    print("inside", num1, num2)
    # pprint(locals())
    return num1 + num2

res1 = sum_numbers(100, 200)
print(f"{num1=} {num2=}")

# pprint(globals())

