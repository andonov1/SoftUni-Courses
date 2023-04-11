class Validator:

    @staticmethod
    def raise_if_string_is_empty_or_whitespace(string, message):
        if string.strip() == '':
            raise ValueError(message)

    @staticmethod
    def raise_if_price_is_invalid(price, message):
        if price <= 0:
            raise ValueError(message)

    @staticmethod
    def raise_if_number_not_in_range(number, min, max, message):
        if number < min or number > max:
            raise ValueError(message)