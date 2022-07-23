def abs_numbers(nums):
    result = [abs(num) for num in nums]
    return result
numbers = list(map(float, input().split(' ')))
print(abs_numbers(numbers))





# ALTERNATE SOLUTION 1:
# numbers = list(map(float, input().split(' ')))
# result = [abs(num) for num in numbers]
# print(result)



# ALTERNATE SOLUTION 2:

# numbers = input().split(' ')
# abs_numbers = []
#
# for num in numbers:
#     abs_numbers.append(abs(float(num)))
#
# print(abs_numbers)

