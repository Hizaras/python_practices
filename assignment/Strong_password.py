import string


def password(strong_password: str):
    validate = True
    lenght = (len(strong_password))
    character = string.punctuation

    if lenght != 7:
        print("Password needs to be 7 digit")
        validate = False

    if not any(lower.islower() for lower in strong_password):
        print("Your Password Should have at least a lower character")
        validate = False

    if not any(upper.isupper() for upper in strong_password):
        print("Sorry your password must have at least an uppercase")
        validate = False

    if not any(integer.isdigit() for integer in strong_password):
        print("Sorry your password must have at least a digit")
        validate = False

    if not any(special_Character in character for special_Character in strong_password):
        print("Sorry your password does not contain any special character")
        validate = False

    if validate:
        print("Password Generated")


storage = str(input("Please enter your password: "))
password(storage)
