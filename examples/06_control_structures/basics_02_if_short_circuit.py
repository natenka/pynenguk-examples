num = input("Enter number: ")

if num.isdigit():
    if 0 <= int(num) <= 200:
        print("Correct")
    else:
        print()
else:
    print("Wrong")
