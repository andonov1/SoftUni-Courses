from abc import ABC, abstractmethod

from robots_manager import Validator


class Booth(ABC):
    def __init__(self, booth_number, capacity):
        self.booth_number = booth_number
        self.capacity = capacity
        self.delicacy_orders = []
        self.price_for_reservation = 0
        self.is_reserved = False

    @property
    def capacity(self):
        return self.__capacity

    @capacity.setter
    def capacity(self, value):
        Validator.raise_if_capacity_invalid(value, "Capacity cannot be a negative number!")
        self.__capacity = value

    @abstractmethod
    def reserve(self, number_of_people):
        ...
