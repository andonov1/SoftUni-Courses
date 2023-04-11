class Validator:

    @staticmethod
    def raise_if_string_is_empty_or_whitespace(string, message):
        if string.strip() == '':
            raise ValueError(message)

    @staticmethod
    def age_validation(age, min_age, message):
        if age < min_age:
            raise ValueError(message)

