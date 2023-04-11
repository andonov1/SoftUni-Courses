from robots_manager import Booth


class OpenBooth(Booth):

    def reserve(self, number_of_people):
        price_per_person = 2.50
        self.price_for_reservation = price_per_person * number_of_people
        self.is_reserved = True