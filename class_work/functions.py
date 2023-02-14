from functools import reduce

def reduce_func(acc, item):
    print(f"acct->{acc} <> item -> {item}")
    return acc + item

print("\n############### Reduce #####################\n")
print(lst)
print(reduce(reduce_func, lst, 100))