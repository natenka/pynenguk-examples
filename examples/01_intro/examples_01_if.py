from pprint import pprint

number = 10
user_num = int(input("Enter number: "))


if user_num == number:
    print("number == 10")
elif user_num >= number:
    print("number >= 10")
elif user_num < number:
    print("number < 10")


print("=" * 40)
