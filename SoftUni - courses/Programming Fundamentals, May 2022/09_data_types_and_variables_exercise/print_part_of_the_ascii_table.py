start = int(input())
end = int(input())
line = ""
for i in range(start, end + 1):
    line += chr(i) + " "
print(line)

# ASCII TABLE:
# ord(string)
# chr(integer)

# ALTERNATE SOLUTION
# for i in range(start, end + 1):
#     print(chr(i), end = " ")

# ALTERNATE SOLUTION:
# print(f"->{line.strip()}<-") - removes white spaces on th left and right
# (стрелкичките са за красота, за да се получи "паразитен интервал")

