
numbers_int = list(map(int, input().split()))

print(f"The minimum number is {min(numbers_int)}")
print(f"The maximum number is {max(numbers_int)}")
print(f"The sum number is: {sum(numbers_int)}")

# ALTERNATE SOLUTION 0.050 (vs.0.030 s above) s
#
# def min_number(a):
#     return min(a)
# def max_number(a):
#     return max(a)
# def sum_of_numbers(a):
#     return sum(a)
#
# numbers_int = list(map(int, input().split()))
#
# print(f"The minimum number is {min_number(numbers_int)}")
# print(f"The maximum number is {max_number(numbers_int)}")
# print(f"The sum number is: {sum_of_numbers(numbers_int)}")