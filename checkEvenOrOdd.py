num = input("Enter a number: ")
if num.isdigit() or (num[0] == '-' and num[1:].isdigit()):
    num = int(num)
    if num % 2 == 0:
        print(f"{num} is even.")
    else:
        print(f"{num} is odd.")
else:
    print("Please enter a valid integer.")# This program checks if a number is even or odd.

# num = int(input("Enter a number: "))
# if num % 2 == 0:
#     print("The number is even.")
# else:
#     print("The number is odd.")