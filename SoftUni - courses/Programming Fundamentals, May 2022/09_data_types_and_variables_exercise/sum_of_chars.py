lines = int(input())
total_sum = 0
for i in range(lines):
    letter = input()
    total_sum += ord(letter)

print(f"The sum equals: {total_sum}")


# ASCII TABLE:
# ord(string)
# chr(integer)
