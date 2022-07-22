factor = int(input())
count = int(input())
my_list = []
for i in range(1, count + 1):
    my_list.append(i * factor)
print(my_list)

# ALTERNATE SOLUTION:
# factor = int(input())
# count = int(input())
# list_of_numbers = list(range(factor, count * factor + 1, factor))
# print(list_of_numbers)
