import math

num1 = int(input("enter first number: "))
num2 = int(input("enter second number: "))


def product(num1, num2: int):
    square_number = num1 * num1
    square_number2 = num2 * num2
    value = square_number * square_number2
    print("The product of squared {} and square {} is {}".format(square_number, square_number2, value))
    # return value


print(product(num1, num2))


def difference(num3, num4: int):
    d_square_number = num3 * num3
    d_square_number2 = num4 * num4
    value2 = d_square_number - d_square_number2
    # return value2
    print(f"The difference of squared {d_square_number} and square {d_square_number2} is {value2}")


print(difference(num1, num2))


def addition(num5, num6: int):
    a_square_number = num5 * num5
    a_square_number2 = num6 * num6
    value3 = a_square_number + a_square_number2
    # return value3
    print(f"The addition of squared {a_square_number} and square {a_square_number2} is {value3}")


print(addition(num1, num2))


def calculate(first_number, second_number):
    squared_first_number = math.pow(first_number, 2)
    squared_second_number = math.pow(second_number, 2)
    print(f"The squared of {first_number} is {squared_first_number}")
    print(f"The squared of {second_number} is {squared_second_number}")

    print(f"The sum of {squared_first_number} and {squared_second_number} is "
          f"{squared_first_number + squared_second_number}")

    print(f"The difference of {squared_first_number} and {squared_second_number} is "
          f"{squared_first_number - squared_second_number}")

    print(f"The product of {squared_first_number} and {squared_second_number} is "
          f"{squared_first_number * squared_second_number}")


user_first_number = int(input("Enter First Number: "))
user_second_number = int(input("Enter Second Number: "))

calculate(user_first_number, user_second_number)
