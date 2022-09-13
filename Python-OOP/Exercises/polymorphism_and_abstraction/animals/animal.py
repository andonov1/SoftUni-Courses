from abc import abstractmethod, ABC


class Animal(ABC):
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    @abstractmethod
    def make_sound(self):
        pass

    @abstractmethod
    def __repr__(self):
        pass
