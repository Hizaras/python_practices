# cont = []
#
# for i in range (1, 11):
#     cont.append(i)
squares = []

for i in range(1, 11):
    squares.append(i ** 2)

cont = [num for num in range(1, 11)]

squares = [num1 ** 2 for num1 in range(1, 11)]
evens = [even for even in range(1, 11) if even % 2 == 0]
even_squared_odd_cubed = [num ** 2 if num % 2 == 0 else num ** 3 for num in range(1, 11)]

print(even_squared_odd_cubed)
print(cont)
print(squares)
print(evens)

names = ['bimpe', 'Banke', 'abimbola', 'kelechi', 'james', 'olalekan', 'Racheal']
my_names = [name for name in names if name.istitle()]
number_of_times = int(input("How many names will you like to enter"))
input_names1 = [input(f"{i + 1}. Name? ") for i in range(5)]
# input_names = [input(f"{i+1}. Name? ") for i in range(number_of_times)]
input_names = [name for name in [input(f"{i + 1}. Name? ") for i in range(number_of_times)] if name.istitle()]

# my_names = []
# for name in names:
#     if name.istitle():
#         my_names.append(name)

print(my_names)
print(input_names1)
print(input_names)

x_and_y = []

# for x in range(1, 5):
#     for y in range(1, 5):
#         x_and_y.append((x, y))

x_and_y = [(x, y) for x in range(1, 6) for y in range(1, 6)]
print(x_and_y)
