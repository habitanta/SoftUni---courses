n = int(input())
COMMAND_EVEN = 'even'
COMMAND_ODD = 'odd'
COMMAND_POSITIVE = 'positive'
COMMAND_NEGATIVE = 'negative'
numbers = []
filtered_numbers = []
for _ in range(n):
    current_num = int(input())
    numbers.append(current_num)
command = input()
for d in numbers:
    filtered_command = (
        (command == COMMAND_EVEN and d % 2 == 0) or
        (command == COMMAND_ODD and d % 2 != 0) or
        (command == COMMAND_POSITIVE and d >= 0) or
        (command == COMMAND_NEGATIVE and d < 0)
    )
    if filtered_command:
        filtered_numbers.append(d)
print(filtered_numbers)