class MyDict(dict):
    def __setitem__(self, key, value):
        if type(key) != str:
            raise TypeError("The value entered is not a string")
        super().__setitem__(key, value)


new_dict = MyDict()
# new_dict[1] = 6
new_dict['hello'] = 6
print(new_dict)
