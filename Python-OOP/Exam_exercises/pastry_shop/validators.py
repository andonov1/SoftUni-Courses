class Validator:

    @staticmethod
    def raise_if_string_is_empty_or_whitespace(string, message):
        if string.strip() == '':
            raise ValueError(message)

    @staticmethod
    def raise_if_value_invalid(value, message):
        if value <= 0:
            raise ValueError(message)

    @staticmethod
    def raise_if_capacity_invalid(value, message):
        if value < 0:
            raise ValueError(message)

    @staticmethod
    def check_if_delicacy_exists(name, directory):
        for obj in directory:
            if name == obj.name:
                return obj

    @staticmethod
    def get_booth(booth_number, directory):
        for booth in directory:
            if booth_number == booth.booth_number:
                return booth

