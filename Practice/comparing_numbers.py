import random

lst = list(range(1, 11))

print(lst)
random.shuffle(lst)

print(lst)
print(random.choice(lst))

# lst.append([20,60,79])

# lst.extend([20, 60, 79])
lst += ([20, 60, 79])

# lst.insert(0, 56)
lst.insert(-1, 56)

last_item = lst.pop()
print(last_item)
print(lst)

item_at_index_0 = lst.pop(0)
print(item_at_index_0)
print(lst)

lst.remove(8)
print(lst)

lst.sort(reverse=True)
print(lst)
