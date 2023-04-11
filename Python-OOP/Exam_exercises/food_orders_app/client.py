class Client:
    def __init__(self, phone_number):
        self.phone_number = phone_number
        self.shopping_cart = []
        self.bill = 0

    @property
    def phone_number(self):
        return self.__phone_number

    @phone_number.setter
    def phone_number(self, value):
        valid = True
        if value[0] != '0' or len(value) != 10:
            valid = False
        for el in value:
            if not el.isdigit():
                valid = False

        if not valid:
            raise ValueError("Invalid phone number!")
        self.__phone_number = value
