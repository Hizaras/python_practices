class Human:

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def full_name(self):
        return f"{self.last_name} {self.first_name}"

    def __str__(self):
        return f"name={self.last_name} {self.first_name}, age={self.age}"


class Manager(Human):
    def __int__(self, first_name: str, last_name: str, age: int, bonus: float):
        self.bonus = bonus
        super().__init__(first_name, last_name)


class Employee(Human):
    pass


employee: Employee = Employee("Hadiza", "Umar", 21)
manager: Manager = Manager("Egusi", "Cappy", 65, 1200)
print(employee.full_name())
print(manager.full_name())

human_list = [employee, manager, Human("Sapien", "Homo", 0, "Unknown")]
for human in human_list:
    print(human.full_name())


    class Practice:
        count = 0

        def __int__(self, first):
            self.first = first

        def play(self):
            return f"Playing with {self.first}"

        @classmethod
        def create(cls, name):
            return cls(name)

        @staticmethod
        def just_here():
            return "Just hanging out here!!!"


    p1 = Practice("Banke")
    p2 = Practice.create("hadiza")
    Practice.just_here()
    p1.just_here()



