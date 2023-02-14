class Human:
    name = 'hadiza'

    def __init__(self, name="", age=0):
        self.name = name
        self.age = age

    def get_name(self):
        return self.name

    @property
    def name(self):
        return self._name

    def get_age(self):
        return self.age

    @property
    def age(self):
        return self.get_age

    @name.setter
    def name(self, name: str):
        print("calling the setter")
        if name.islower():
            raise ValueError("Name cannot be all lower case")
        self.name = name

    @age.setter
    def age(self, age: int):
        print("calling the setter")
        self.age = age

    @name.deleter
    def name(self):
        print("deleting...")
        del self._name


h1 = Human()
print(h1.get_name())
print(h1.name)
h1.set_name("Rachel")
print(h1.get_name())
