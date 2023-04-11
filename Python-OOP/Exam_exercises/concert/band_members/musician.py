from abc import ABC, abstractmethod

from exams.concert.validators import Validator


class Musician(ABC):
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.skills = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        Validator.raise_if_string_is_empty_or_whitespace(value, "Musician name cannot be empty!")
        self.__name = value

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        Validator.age_validation(value, 16, "Musicians should be at least 16 years old!")
        self.__age = value

    @abstractmethod
    def learn_new_skill(self, new_skill):
        ...
