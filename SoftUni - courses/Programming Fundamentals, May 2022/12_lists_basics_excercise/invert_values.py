numbers = input().split()
opposite_numbers = []
for i in numbers:
    opposite_numbers.append(-int(i))
print(opposite_numbers)

# ALTERNATE SOLUTION
# for current_index in range(len(numbers)):
#     current_number = int(numbers[current_index])
#     opposite_numbers.append(-current_number)
# print(opposite_numbers)