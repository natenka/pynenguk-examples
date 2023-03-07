from pprint import pprint


numbers = [10, 20, 30]
num_list = []

num_list.append(str(numbers[0]))
num_list.append(str(numbers[1]))
num_list.append(str(numbers[2]))

print(num_list)

# for
numbers = [10, 20, 30]
num_list = []

for num in numbers:
    print(num)
    num_list.append(str(num))

print(num_list)
