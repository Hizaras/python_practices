class DoubleIt(int):
    def __new__(cls, value):
        return super().__new__(cls, value * 2)


class MyList(list):
    def __setitem__(self, key, value):
        if key < 1:
            raise IndexError("Index can neither be negative nor zero")
        super().__setitem__(key - 1, value)

    def __getitem__(self, item):
        if item < 1:
            raise IndexError("Index can neither be negative nor zero")
        super().__getitem__(item - 1)


new_list = MyList("hello")
print(new_list)
new_list[1] = 20
print(new_list)
