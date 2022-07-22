from math import ceil
number_of_people = int(input())
capacity_of_persons = int(input())
print(ceil(number_of_people / capacity_of_persons))

#Alternate soution, considering zero capacity:

# from math import ceil
# number_of_people = int(input())
# capacity_of_persons = int(input())
# courses = 0
# if capacity_of_persons != 0:
#     courses = ceil(number_of_people / capacity_of_persons)
# print(courses)

# ALternate solution 2

# from math import ceil
# number_of_people = int(input())
# capacity_of_persons = int(input())
# courses = 0 if capacity_of_persons == 0 else ceil(number_of_people / capacity_of_persons)
# print(courses)



