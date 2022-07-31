

def divide(a,indx, part):
    position_index = indx
    divisor = len(a[indx]) // part
    if len(a[indx]) % part == 0:
        for i in range(0, len(a[indx]), divisor):
            position_index += 1
            a.insert(position_index, a[indx][i:i + divisor])
        a.pop(indx)
        return a
    else:
        excess = len(a[indx]) % part
        for i in range(0, len(a[indx]) - excess, divisor):
            position_index += 1
            a.insert(position_index, a[indx][i:i + divisor])
        a[indx + part] += a[indx][-excess::]
        a.pop(indx)
        return a

def merge(words, start, end):
    words[start:end + 1] = ["".join(words[start:end + 1])]


    return words


strings = input().split()

while True:
    command = input().split()
    action = command[0]
    if action == "3:1":
        break
    elif action == "merge":
        start_index = int(command[1])
        end_index = int(command[2])
        if start_index < 0:
            start_index = 0
        if end_index > len(strings):
            end_index = len(strings) - 1
        strings = merge(strings,start_index, end_index)

    elif action == "divide":
        index = int(command[1])
        partitions = int(command[2])
        strings = divide(strings, index, partitions)

print(' '.join(strings))

# ALTERNATE SOLUTION BY A COLLEAGUE:
# def merge(words, start, end):
#     if start < 0:
#         start = 0
#     if end > len(words):
#         end = len(words)
#     words[start:end + 1] = ["".join(words[start:end + 1])]
#     return words
#
#
# def divide(words, i, parts):
#     popped_word = words.pop(i)
#     divided_words = []
#     counter = 0
#     number_of_chars = len(popped_word) // parts
#
#     for p in range(parts):
#         if p == parts - 1:
#             divided_words.append(popped_word[counter:])
#             break
#         divided_words.append(popped_word[counter:counter + number_of_chars])
#         counter += number_of_chars
#
#     for index in range(len(divided_words)):
#         words.insert(index + i, divided_words[index])
#
#     return words
#
#
# words_input = input().split()
# command = input()
#
# while command != "3:1":
#     data = command.split()
#     action = data[0]
#     if action == "merge":
#         start_index, end_index = int(data[1]), int(data[2])
#         data = merge(words_input, start_index, end_index)
#     elif action == "divide":
#         index, partitions = int(data[1]), int(data[2])
#         data = divide(words_input, index, partitions)
#
#     command = input()
#
# print(" ".join(words_input))