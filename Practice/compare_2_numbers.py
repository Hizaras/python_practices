num1 = int(input("enter first number: "))
num2 = int(input("enter second number: "))


def check_numbers(num1, num2: int):
    if num1 == num2:
        print("true")
    else:
        print("false")


check_numbers(num1, num2)
