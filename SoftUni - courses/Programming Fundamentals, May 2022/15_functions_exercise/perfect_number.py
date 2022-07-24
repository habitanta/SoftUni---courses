def find_divisors(a):
    divisors = []
    for number in range(1, a):
        if a % number == 0:
            divisors.append(number)
    return divisors


number = int(input())
returned_number = sum(find_divisors(number))
if number == int(returned_number):
    print("We have a perfect number!")
else:
    print("It's not so perfect.")


# ALTERNATE SOLUTION:
#
# def is_perfect_number(a):
#     sum = 0
#     for divisor  in range(1, a):
#         if number % divisor == 0:
#             sum += divisor
#     if number == sum:
#         return "We have a perfect number!"
#     return "It's not so perfect."
#
#
# number = int(input())
# print(is_perfect_number(number))






