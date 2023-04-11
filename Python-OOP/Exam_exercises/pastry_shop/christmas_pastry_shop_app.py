from robots_manager import OpenBooth
from robots_manager import PrivateBooth
from robots_manager import Gingerbread
from robots_manager import Stolen
from robots_manager import Validator


class ChristmasPastryShopApp:
    def __init__(self):
        self.booths = []
        self.delicacies = []
        self.income = 0

    def add_delicacy(self, type_delicacy, name, price):
        delicacies = {'Gingerbread': Gingerbread,
                      'Stolen': Stolen}
        if Validator.check_if_delicacy_exists(name, self.delicacies):
            raise Exception(f"{name} already exists!")

        if type_delicacy not in delicacies:
            raise Exception(f"{type_delicacy} is not on our delicacy menu!")

        current_delicacy = delicacies[type_delicacy](name, price)
        self.delicacies.append(current_delicacy)
        return f"Added delicacy {name} - {type_delicacy} to the pastry shop."

    def add_booth(self, type_booth, booth_number, capacity):
        booths = {"Open Booth": OpenBooth,
                  "Private Booth": PrivateBooth}

        current_booth = Validator.get_booth(booth_number, self.booths)
        if current_booth:
            raise Exception(f"Booth number {booth_number} already exists!")

        if type_booth not in booths:
            raise Exception(f"{type_booth} is not a valid booth!")

        current_booth = booths[type_booth](booth_number, capacity)
        self.booths.append(current_booth)
        return f"Added booth number {booth_number} in the pastry shop."

    def reserve_booth(self, number_of_people):
        for booth in self.booths:
            if not booth.is_reserved and booth.capacity >= number_of_people:
                booth.reserve(number_of_people)
                return f"Booth {booth.booth_number} has been reserved for {number_of_people} people."

        raise Exception(f"No available booth for {number_of_people} people!")

    def order_delicacy(self, booth_number, delicacy_name):

        current_booth = Validator.get_booth(booth_number, self.booths)
        current_delicacy = Validator.check_if_delicacy_exists(delicacy_name, self.delicacies)

        if not current_booth:
            raise Exception(f"Could not find booth {booth_number}!")

        if not current_delicacy:
            raise Exception(f"No {delicacy_name} in the pastry shop!")

        current_booth.delicacy_orders.append(current_delicacy)
        return f"Booth {booth_number} ordered {delicacy_name}."

    def leave_booth(self, booth_number):
        current_booth = Validator.get_booth(booth_number, self.booths)

        self.income += current_booth.price_for_reservation
        orders = 0

        for delicacy in current_booth.delicacy_orders:
            orders += delicacy.price
        self.income += orders

        current_booth.is_reserved = False
        current_booth.price_for_reservation = 0
        current_booth.delicacy_orders = []

        return f"Booth {booth_number}:\n" \
               f"Bill: {self.income:.2f}lv."

    def get_income(self):
        return f"Income: {self.income:.2f}lv."

