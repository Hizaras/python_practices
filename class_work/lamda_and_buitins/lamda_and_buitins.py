def add(a: int, b: int) -> int:
    """Adds two numbers"""
    return a + b


# print(add.__name__)
# print(add.__doc__)
# print(add.__annotations__)

def operate(x, y, func):
    return func(x, y)


print(operate(2, 3, add))


def sub(x, y):
    return y - x


print(operate(5, 8, sub))


def multiply(a):
    def by(b):
        return a * b

    return by

    # def multiply(a):
    # def by(b):
    #     def another(c):
    #         return a * b * c
    #     return another
    #
    # return by


multiply_by_five = multiply(5)(6)

# print(multiply_by_five(6))

adder = lambda a, b: a + b
# print(add.__name__)


print(adder(10, 9))
print(operate(2, 3, adder))
print(operate(2, 3, lambda a, b: a + b))
print(operate(2, 3, lambda a, b: a - b))
print(operate(2, 3, lambda w, y: w * y))
# print(operate(2,3, lambda a, b: 5 * 9))
#
# import builtins
#
# sum = 67
#
# print(builtins.sum([1, 2, 3]))
# builtins.


print(operate(2, 3, lambda w, y: w * y))
# import builtins

# print(round(56.67854, -2))

arr = [1, 6, 4, 7, 2]
print(sum(arr, 100))

letters = [['a'], ['b', 'c'], ['d'], ['e', 'f']]
print(sum(letters, []))
print(max([1, 2, 3, 4, 5, 6]))
fruits = "apple pear cucumber mango grape melon".split()
print(max(fruits))
print(min(fruits))
print(max(fruits, key=len))
print(min(fruits, key=len))
print(max(fruits, key=lambda x: x[-3:]))

users = [
    {'name': 'Ibrahim',
     'age': 32,
     'gender': 'male',
     'user_name': 'Ibro',
     'is_verified': False,
     'tweets': [
         {'content': 'PO for President', 'likes': 450, 'retweets': 233},
         {'content': 'Atiku is our man', 'likes': 4, 'retweets': 12}
     ]
     },

    {'name': 'Racheal',
     'age': 21,
     'gender': 'Female',
     'user_name': 'betty',
     'is_verified': False,
     'tweets': [
         {'content': '', 'likes': 450, 'retweets': 233},
         {'content': 'Thinking about amez', 'likes': 4, 'retweets': 2},
         {'content': 'Amazing grace', 'likes': 2000, 'retweets': 1542}
     ]
     },

    {'name': 'James',
     'age': 25,
     'gender': 'male',
     'user_name': 'amez',
     'is_verified': True,
     'tweets': [
         {'content': 'Love is life', 'likes': 66, 'retweets': 89},
         {'content': 'only Racheal i know', 'likes': 97, 'retweets': 2}
     ]
     },

    {'name': 'Dorris',
     'age': 16,
     'gender': 'Female',
     'user_name': 'anything',
     'is_verified': False,
     'tweets': [
         {'content': 'i love chimamanda Adichie', 'likes': 450, 'retweets': 233},
         {'content': ' Feminism is the goal', 'likes': 4, 'retweets': 2}
     ]
     },

    {'name': 'Jacob',
     'age': 37,
     'gender': 'male',
     'user_name': 'elder_j',
     'is_verified': True,
     'tweets': [
         {'content': 'Reflection is my goal', 'likes': 5, 'retweets': 3},
         {'content': 'How to get more likes on twitter', 'likes': 1, 'retweets': 1}
     ]
     },

    {'name': 'Derrick',
     'age': 29,
     'gender': 'Male',
     'user_name': 'standby_gen',
     'is_verified': False,
     'tweets': [
     ]
     },

    {'name': 'Mubarak',
     'age': 47,
     'gender': 'Male',
     'user_name': 'Whistle',
     'is_verified': True,
     'tweets': [

     ]
     },

    {'name': 'Elijah',
     'age': 16,
     'gender': 'male',
     'user_name': 'el_di_si',
     'is_verified': True,
     'tweets': [
         {'content': 'PO for President', 'likes': 450, 'retweets': 233},
         {'content': 'Atiku is our man', 'likes': 4, 'retweets': 2}
     ]
     },

    {'name': 'Hadizaa',
     'age': 21,
     'gender': 'Female',
     'user_name': 'deeza',
     'is_verified': True,
     'tweets': [
         {'content': 'PO for President', 'likes': 450, 'retweets': 233},
         {'content': 'Atiku is our man', 'likes': 4, 'retweets': 2}
     ]
     }
]

no_of_users = len(users)
user_names = {user['user_name'] for user in users}
female_users = [user['name'] for user in users if user['gender'] == 'Female']
inactive_users = [user for user in users if len(user['tweets']) == 0]
name_and_age = [{'name': user['name'], 'age': user['age']} for user in users]
avrg_age_of_users = round(sum(user['age'] for user in users) / len(users))
print(name_and_age)
print(female_users)

print(max(users, key=lambda x: x['age']))
print(max(users, key=lambda x: len(x['tweets'])))

# iterable1 = (1, 2, 3, 4)
# iterable2 = ('hello', 'how', 'are', 'you')
# print(list(zip(iterable2, iterable1,)))
iterable1 = (1, 2, 3)
iterable2 = ('hello', 'how', 'are', 'you')
print(list(zip(iterable2, iterable1, iterable2)))
print(sorted('helloAz', reverse=True))
print(sorted(fruits, key=len))
print(sorted(fruits, key=lambda x: x[-1]))

# print(sum([user['age'] for user in users]) / len(users))
# print(any(user['is verified']for user in users))
# print(all(user['is verified']for user in users))
lst = [1, 2, 3, 4, 5, ]
print(list(map(lambda x: x ** 2, [1, 2, 3, 4, 5, ])))
print([x ** 2 for x in lst])
print(list(map(str.upper, fruits)))
print(list(map(lambda x: x.upper(), fruits)))
fruits.append('Agbado')

print(list(map(str.istitle, fruits)))
print(list(filter(str.istitle, fruits)))
print(list(map(lambda y: y.upper(), filter(lambda x: not x.istitle(), fruits))))
print([x.upper() for x in fruits if not x.istitle()])

from functools import reduce

print(reduce(lambda acc, item: acc + item, lst))

from functools import reduce


def reduce_func(acc, item):
    print(f"acct->{acc} <> item -> {item}")
    return acc + item


from math import prod

print("\n############### Reduce #####################\n")
print(lst)
print(reduce(reduce_func, lst, 100))
print(sum(lst, 100))
print(prod(lst, start=100))

# using match in python
print("#################  match ######################")

num = int(input("Enter Number: "))
match num:
    case 1:
        print(1)
    case 2:
        print(2)
    case 3:
        print(3)
    case _:
        print("Dont know you")

num = int(input("Enter A Number: "))
match num:
    case _ as x if 1 <= x <= 10:
        print(x)
    case _ as x if 11 <= x <= 20:
        print(x)
    case 30 | 40 | 50:
        print(x)
    case _:
        print("Dont Know you")

lst = [20, 13, "good"]

match lst:
    case [x, y, int(z)]:
        print(x, z, y)
    case [a, [b, c], d]:
        print(a, b, c, d)
    case _:
        print("Nothing matched")


# d = {
#     "name": "Hadiza",
#     "age":
# }

def fizzbuz(num):
    three = num % 3
    five = num % 5
    match (three, five):
        case (0, 0):
            return "FizzBuzz"
        case (0, _):
            return "Fizz"
        case (_, 0):
            return "Buzz"
        case _:
            return num


for i in range(1, 101):
    print(fizzbuz(i))


def suming_list(list_: list[int]) -> int | None:
    match list_:
        case []:
            return 0
        case [first_value, *another_list]:
            return first_value + suming_list(another_list)
        case _:
            print("Can only accept an int")
            return None

import  itertools
print(suming_list([1, 2, 3, 4, 5]))
print(list(itertools.zip_longest([1, 2], [3, 4, 5], fillvalue=0)))
