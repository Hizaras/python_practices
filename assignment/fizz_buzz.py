for counter in range (0, 100):

    if counter % 3 == 0 and counter % 5 == 0:
        print("Fizz Buzz")

    elif counter % 5 == 0:
        print("Buzz")

    elif counter % 3 == 0:
        print("Fizz")

    else:
        print(counter)