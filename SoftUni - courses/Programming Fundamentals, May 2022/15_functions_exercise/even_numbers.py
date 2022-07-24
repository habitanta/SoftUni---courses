numbers_as_digits = [int(s) for s in input().split()]
is_even = lambda x: x % 2 == 0
result = list(filter(is_even, numbers_as_digits))
print(result)

# numbers = [int(s) for s in input().split()]
# even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
#
# print(numbers)


# ALTERNATE SOLUTION

# numbers = input().split()
# numbers_as_digits = []
# for number in numbers:
#     numbers_as_digits.append(int(number))
# etc...


# ALTERNATE SOLUTION

# def even_number(num):
#     new_list = list(filter(lambda x: x % 2 == 0, num))
#     return new_list
#
#
# numbers = list(map(int, input().split()))
# print(even_number(numbers))


# ALTERNATE SOLUTION

# numbers_as_digits = [int(s) for s in input().split()]
# is_even = lambda x: x % 2 == 0
# result = list(filter(is_even, numbers_as_digits))
# print(result)


# ALTERNATE SOLUTION:

# def check_even(number):
#     if number % 2 == 0:
#           return True
#
#     return False
#
# numbers = [int(s) for s in input().split()]
# even_numbers = list( filter(check_even, numbers))
#
# print(even_numbers)

