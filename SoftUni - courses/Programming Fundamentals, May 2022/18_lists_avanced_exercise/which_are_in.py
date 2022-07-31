first_line_str = input().split(", ")
second_line_str = input().split(", ")
substrings = [x for x in first_line_str if any(x in w for w in second_line_str)]
print(substrings)

# ALTERNATE SOLUTION:
#
# version = input()
# new_version = ".".join([x for x in str(int(version.replace(".", "")) + 1)])
# print(new_version)




# ALTERNATE SOLUTION WITH FUNCTION:
#
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

# ANOTHER ALTERNATE SOLUTION:
#
# first_line_str = input().split(", ")
# second_line_str = input().split(", ")
# result = [x for x in first_line_str if x in " ".join(second_line_str)]
# print(result)


# ALTERNATE SOLUTION:
#
# first_line_str = input().split(", ")
# second_line_str = input().split(", ")
# result = []
# for x in first_line_str:
#     if x in " ".join(second_line_str):
#         result.append(x)
# print(result)

# print(substrings)


# ALTERNATE AND RECOMMENDED SOLUTION WITH FOR CYCLES:

# first_line_str = input().split(", ")
# second_line_str = input().split(", ")
# substrings = []
# for first_word in first_line_str:
#     for second_word in second_line_str:
#         substrings.append(first_word)
#          break
# print(substrings)