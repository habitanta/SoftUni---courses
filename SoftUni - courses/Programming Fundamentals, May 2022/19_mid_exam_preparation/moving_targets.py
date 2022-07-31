
targets = list(map(int, input().split()))

while True:
    command = input()
    if command == "End":
        print("|".join(map(str, targets)))
        break
    command = command.split()
    action = command[0]
    index = int(command[1])
    if action == "Shoot":
        power = int(command[2])
        if 0 <= index < len(targets):
            targets[index] -= power
            if targets[index] <= 0:
                targets.pop(index)
        else:
            continue
    elif action == "Add":
        value = int(command[2])
        if 0 <= index < len(targets):
            targets.insert(index, value)
            if int(targets[index]) <= 0:
                targets.pop(index)
        else:
            print("Invalid placement!")
            continue
    elif action == "Strike":
        radius = int(command[2])
        if index >= 0:
            if index - radius >= 0 and index + radius < len(targets):
                for i in range(index - radius, index + radius + 1):
                    targets.pop(index - radius)
            else:
                print("Strike missed!")
                continue

