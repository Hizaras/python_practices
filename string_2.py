import string

abc = string.ascii_lowercase

word = "love"
k = 5

encoded = word.translate(str.maketrans(abc[:-5], abc[5:]))
print(encoded)


