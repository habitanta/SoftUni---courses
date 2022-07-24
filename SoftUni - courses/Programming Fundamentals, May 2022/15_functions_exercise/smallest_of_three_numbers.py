def min_number_func(num_1, num_2, num_3):
    return min(num_1, num_2, num_3)


a = int(input())
b = int(input())
c = int(input())

print(min_number_func(a, b, c))



# ALTERNATE SOLUTION WITH LIST:
def min_number_func(some_numbers):
    return min(some_numbers)


a = int(input())
b = int(input())
c = int(input())
list_of_numbers = [a, b, c]
print(min_number_func(list_of_numbers))