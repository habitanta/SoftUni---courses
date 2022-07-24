def sum_numbers(a, b):
    return a + b
def subtract(a, b):
    return a - b

def add_and_subtract(a, b, c):
    add = sum_numbers(a, b)
    result = subtract(add, c)
    return result


first_num = int(input())
second_num = int(input())
third_num = int(input())


print(add_and_subtract(first_num, second_num, third_num))