
def sum_of_even_and_odd(a):
    list_of_a = list(map(int,str(a)))
    sum_of_odd_digits = 0
    sum_of_even_digits = 0
    for element in list_of_a:
        if element % 2 == 0:
            sum_of_even_digits += element
        else:
            sum_of_odd_digits += element
    return f"Odd sum = {sum_of_odd_digits}, Even sum = {sum_of_even_digits}"

number = int(input())
print(sum_of_even_and_odd(number))

# ALTERNATE METHOD OF SEPARATING DIGITS FROM AN INTEGER:
#
# def sum_of_even_and_odd(a):
# >>>!list_of_a = [*map(int,str(a))] !<<<
#     sum_of_odd_digits = 0
#     sum_of_even_digits = 0
#     etc...


# ALTERNATE METHOD OF SEPARATING DIGITS FROM AN INTEGER:
#
# def sum_of_even_and_odd(a):
#     list_of_a = [int(i) for i in str(a)]
#     sum_of_odd_digits = 0
#     sum_of_even_digits = 0
#     etc...


#  ALTERNATE METHOD OF SEPARATING DIGITS FROM AN INTEGER:
# def sum_of_even_and_odd(a):
#     list_of_a = list(map(int,' '.join(str(a)).split()))
#     sum_of_odd_digits = 0
#     sum_of_even_digits = 0
#    etc...