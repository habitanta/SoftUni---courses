
def password_validator(a):
    validity = True
    digits_counter = 0
    if 6 > len(a) or len(a) > 10:
        validity = False
        print("Password must be between 6 and 10 characters")
    if a.isalnum() == False:
        validity = False
        print("Password must consist only of letters and digits")
    for character in a:
        if character.isdigit():
            digits_counter += 1
    if digits_counter < 2:
        validity = False
        print("Password must have at least 2 digits")
    if validity == True:
        print("Password is valid")
password = input()
password_validator(password)


# ALTERNATE QUICKER SOLUTION (0.040 s vs 0.060s):
#
# def length_is_valid(some_string):
#     if 6 <= len(some_string) <= 10:
#         return  True
#     print("Password must be between 6 and 10 characters")
#     return False
#
# def symbols_are_valid(some_string):
#     if some_string.isalnum():
#         return True
#     print("Password must consist only of letters and digits")
#     return False
#
#
# def have_at_least_two_digits(some_string):
#     digits_counter = 0
#     for character in some_string:
#         if character.isdigit():
#             digits_counter += 1
#     if digits_counter >= 2:
#         return True
#     print("Password must have at least 2 digits")
#     return False
#
# some_pass = input()
#
# validated = [length_is_valid(some_pass),\
#              symbols_are_valid(some_pass),\
#              have_at_least_two_digits(some_pass)]
# if all(validated):
#     print("Password is valid")


