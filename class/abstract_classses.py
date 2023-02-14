import abc


# class Mammal(metaclass=abc.ABCMeta):
class Mammals(abc.ABC):
    @abc.abstractmethod
    def move(self):
        pass


class Person(Mammals):
    def move(self):
        pass


p1 = Person()
