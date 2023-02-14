x_and_y = []

for x in range(1, 5):
    for y in range(1, 5):
        x_and_y.append((x, y))

x_and_y = [(x, y) for x in range(1, 6) for y in range(1, 6)]
print(x_and_y)

listcomp = [num % 3 for num in range(1, 10)]
setcomp = {num % 3 for num in range(1, 10)}
dictcomp = {k: v for k, v in enumerate(range(11, 16), 11)}
dictcomp1 = {k: v for k, v in enumerate("Banke", 11)}

genexp = (num for num in range(1, 6))

print(type(listcomp), listcomp)
print(type(setcomp), setcomp)
print(type(dictcomp), dictcomp)
print(type(dictcomp1), dictcomp1)
print(type(genexp), genexp)

# print(next(genexp))
# print(next(genexp))
# print(next(genexp))
print(list(genexp))
# print((i for i in range(100000000000)))
genexp = (i for i in range(100000000000))

for i in genexp:
    print(i)
