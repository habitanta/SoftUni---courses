train = int(input())
wagons = [0] * train
command = input()

while command != "End":
    result = command.split()
    if "add" in command:
        people = int(result[1])
        wagons[- 1] += people
    elif "insert" in command:
        wagon_index = int(result[1])
        people = int(result[2])
        wagons[wagon_index] += people
    elif "leave" in command:
        wagon_index = int(result[1])
        people = int(result[2])
        wagons[wagon_index] -= people
    command = input()

print(wagons)



# train = int(input())
# # wagons = list(map(int, train * str(0)))
# # wagons = [int(x) for x in train * str(0)
# wagons = [0] * train
# command = input()
#
#
# while command != "End":
#   result = command.split()
#     if "add" in command:
#         people = int(result[1])
#         wagons.append(people + wagons[train - 1])
#         wagons.pop(train - 1)
#     elif "insert" in command:
#         wagon_index = int(result[1])
#         people = int(result[2])
#         wagons.insert(wagon_index, wagons[wagon_index] + people)
#         wagons.pop(wagon_index + 1)
#     elif "leave" in command:
#         wagon_index = int(result[1])
#         people = int(result[2])
#         wagons.insert(wagon_index, wagons[wagon_index] - people)
#         wagons.pop(wagon_index + 1)
#     command = input()
#
#
# print(wagons)


