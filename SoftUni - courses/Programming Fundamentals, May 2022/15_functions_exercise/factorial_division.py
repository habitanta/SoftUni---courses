def division(a, b):
    return a / b
def factorial_find(a):
    for number in range(1, a):
        a *= number
    return a
first_num = int(input())
second_num = int(input())
print(f"{division(factorial_find(first_num), factorial_find(second_num)):.2f}")


# ALTERNATE BUT SLOWER SOLUTION 0.050 s vs 0.080 s
#
# def factorial_find(a):
#     for number in range(1, a):
#         a *= number
#     return a
# first_num = int(input())
# second_num = int(input())
# first_factorial = factorial_find(first_num)
# second_factorial = factorial_find(second_num)
# result = first_factorial / second_factorial
# print(f"{result:.2f}")




# JUST A POSSIBILITY:
#
    # factorial = a
    # for number in range(a - 1,0,-1):
    #     factorial *= number
    # return factorial



