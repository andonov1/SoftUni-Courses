from abc import ABC, abstractmethod

from exams.bakery.common.validators import Validator


class Table(ABC):
    def __init__(self, table_number, capacity):
        self.table_number = table_number
        self.capacity = capacity
        self.food_orders = []
        self.drink_orders = []
        self.number_of_people = 0
        self.is_reserved = False

    @property
    def capacity(self):
        return self.__capacity

    @capacity.setter
    def capacity(self, value):
        Validator.raise_if_price_is_invalid(value, "Capacity has to be greater than 0!")
        self.__capacity = value

    @property
    @abstractmethod
    def min_table_number(self):
        pass

    @property
    @abstractmethod
    def max_table_number(self):
        pass

    @property
    @abstractmethod
    def table_message(self):
        pass

    @property
    def table_number(self):
        return self.__table_number

    @table_number.setter
    def table_number(self, value):
        Validator.raise_if_number_not_in_range(value, self.min_table_number, self.max_table_number, self.table_message)
        self.__table_number = value

    def reserve(self, number_of_people):
        self.is_reserved = True
        self.number_of_people += number_of_people

    def order_food(self, baked_food):
        self.food_orders.append(baked_food)

    def order_drink(self, drink):
        self.drink_orders.append(drink)

    def get_bill(self):
        result = 0
        for drink in self.drink_orders:
            result += drink.price
        for food in self.food_orders:
            result += food.price
        return result

    def clear(self):
        self.food_orders = []
        self.drink_orders = []
        self.number_of_people = 0
        self.is_reserved = False

    def free_table_info(self):
        if not self.is_reserved:
            return f"Table: {self.table_number}\n" \
                   f"Type: {self.__class__.__name__}\n" \
                   f"Capacity: {self.capacity}"
