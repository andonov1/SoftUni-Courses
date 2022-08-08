def password_validator(password):
    is_valid = True
    if not 6 <= len(password) <= 10:
        print("Password must be between 6 and 10 characters")
        is_valid = False
    if not password.isalnum():
        print("Password must consist only of letters and digits")
        is_valid = False

    digits_cnt = 0
    for i in range(len(password)):
        if password[i].isdigit():
            digits_cnt += 1
    if digits_cnt < 2:
        print("Password must have at least 2 digits")
        is_valid = False
    if is_valid:
        return True






given_password = input()
if password_validator(given_password):
    print("Password is valid")