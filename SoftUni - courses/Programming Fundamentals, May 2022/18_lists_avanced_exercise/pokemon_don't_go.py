def increase_decrease(sequence_of_elements, comparison):
    i = 0
    for x in sequence_of_elements:
            if x > comparison:
                sequence_of_elements[i] -= comparison
            elif x <= comparison:
               sequence_of_elements[i] += comparison
            i += 1
    return sequence_of_elements


pockemon_distance = list(map(int,input().split()))
sum_of_removed = 0
while len(pockemon_distance) != 0:
    index = int(input())
    if index < 0:
        pockemon_distance.insert(0, pockemon_distance[-1])
        removed_element = pockemon_distance.pop(1)


    elif index > len(pockemon_distance) - 1:
        pockemon_distance.append(pockemon_distance[0])
        removed_element = pockemon_distance.pop(-2)

    else:
        removed_element = pockemon_distance.pop(index)


    pockemon_distance = increase_decrease(pockemon_distance, removed_element)
    sum_of_removed += removed_element

print(sum_of_removed)



