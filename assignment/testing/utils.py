# def add(x, y):
#     assert isinstance(x, (int, float)) and isinstance(y, (int, float)), "Only int or float can be added"
#     assert x > 0 and y > 0, "numbers cannot be negative"
#     return x + y
#
#
#
# print(add('jhg', 'jhg'))


def add(lst: list) -> int:
    assert isinstance(lst, list), "Only list"
    return sum(lst)


print(add(['22', '23', '5']))
