gifts = input().split()
command = input()
while command != "No Money":
    new_split = command.split(" ")
    instruction = new_split[0]
    value = new_split[1]
    if instruction == "OutOfStock":
        while value in gifts:
            current_index = gifts.index(value)
            gifts[current_index] = "None"
    elif instruction == "Required":
        index = int(new_split[2])
        if 0 <= index <= len(gifts) - 1:
            gifts[index] = value
        else:
            command = input()
            continue
    elif instruction == "JustInCase":
        gifts.pop()
        gifts.append(value)
    else:
        command = input()
        continue
    command = input()
while "None" in gifts:
    gifts.remove("None")
print(" ".join(gifts))

