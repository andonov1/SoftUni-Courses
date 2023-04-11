from abc import ABC, abstractmethod

from robots_manager import Validator


class Delicacy(ABC):
    def __init__(self, name, portion, price):
        self.name = name
        self.portion = portion
        self.price = price

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        Validator.raise_if_string_is_empty_or_whitespace(value, "Name cannot be null or whitespace!")
        self.__name = value

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        Validator.raise_if_value_invalid(value, "Price cannot be less or equal to zero!")
        self.__price = value

    @abstractmethod
    def details(self):
        ...
