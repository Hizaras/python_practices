def last_elem(string):
    return string[-1]
fruits = ['banana', 'apple', 'cucumber', 'mango', 'grape']
# fruits.sort(key=len)
fruits.sort(key=last_elem, reverse=True)
print(fruits)
