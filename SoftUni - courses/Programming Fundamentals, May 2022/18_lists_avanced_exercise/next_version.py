# def version_upgrade(a):
#     for index in range(len(a) - 1, -1, -1):
#         if a[index] > 9:
#             a[index] = 0
#             a[index - 1] += 1
#     return a
#
# initial_version = [int(x) for x in input().split(".")]
# initial_version[-1] += 1
# new_version = ".".join(list(map(str, version_upgrade(initial_version))))
#
# print(new_version)

initial_version = int("".join(input().split(".")))
initial_version += 1
print(initial_version)

version = input()



# ALTERNATE SOLUTION WITH FOR CYCLE:

# initial_version = [int(x) for x in input().split(".")]
# initial_version[-1] += 1
# for index in range(len(initial_version) - 1, -1, -1):
#     if initial_version[index] > 9:
#         initial_version[index] = 0
#         if index - 1 >=0:
#             initial_version[index - 1] += 1
# new_version = ".".join(list(map(str, initial_version)))
#
# print(new_version)


# ALTERNATE SOLUTION WITH IF'S:
#
# initial_version = [int(x) for x in input().split(".")]
# initial_version[-1] += 1
# if initial_version[-1] > 9:
#     initial_version[-1] = 0
#     initial_version[-2] += 1
# if initial_version[-2] > 9:
#     initial_version[-2] = 0
#     initial_version[-3] += 1
# new_version = ".".join(list(map(str, initial_version)))
#
# print(new_version)



