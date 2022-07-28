

# MY SOLUTION

notes = input()
list_of_numbers = []
list_of_tasks = []
while not "End" == notes:
    unpack = notes.split("-")
    importance = int(unpack[0])
    note = unpack[1]
    list_of_numbers.append(importance)
    list_of_numbers.sort()
    index = list_of_numbers.index(importance)
    list_of_tasks.insert(index, note)
    notes = input()
print(list_of_tasks)


# ALTERNATE SOLUTION WITH TUPLE:
# tasks = []
#
# while True:
#     command = input().split("-")
#
#     if command [0] == "End":
#         break
#     priority = int(command[0])
#     task = command[1]
#     tasks.append((priority, task))
# sorted_tasks = [task_data[1] for task_data in sorted(tasks)]
#
# print(sorted_tasks)

# ALTERNATE SOLUTION:
#
#
# notes = [0] * 10
#
# while True:
#     command = input()
#     if command == "End":
#         break
#     tokens = command.split("-")
#     priority = int(tokens[0]) - 1
#     note  = tokens[1]
#     notes.pop(priority)
#     notes.insert(priority,note)
# result = [element for element in notes if element != 0]
# print(result)



# ANOTHER ALTERNATE SOLUTION:


# todo_list = []
#
# while True:
#     task = input().split("-")
#
#     if task [0] == "End":
#         break
#     todo_list.append([int(task[0]), task[1]])
#
# todo_list.sort(key=lambda x: x[0])
# # mylist = [[7, 8], [1, 2, 3], [2, 5, 6]]
# # # list(map(lambda x: x[1], mylist)) returns [8, 2 ,5]
# todo_list = [item[1] for item in todo_list]
# print(todo_list)

