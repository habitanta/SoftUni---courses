people_in_queue = int(input())

current_state_of_the_lift = list(map(int, input().split()))

for wagon in range(len(current_state_of_the_lift)):
    if current_state_of_the_lift[wagon] < 4:
        diff = 4 - int(current_state_of_the_lift[wagon])
        if people_in_queue >= diff:
            current_state_of_the_lift[wagon] += diff
            people_in_queue -= diff
        else:
            current_state_of_the_lift[wagon] += people_in_queue
            people_in_queue = 0
            break
    else:
        continue
full_train = False
if all(x == 4 for x in current_state_of_the_lift):
    full_train = True

current_state_of_the_lift = ' '.join(map(str,current_state_of_the_lift))
if people_in_queue == 0 and full_train == False:
    print(f"The lift has empty spots!")
    print(current_state_of_the_lift)
elif people_in_queue != 0 and full_train == True:
    print(f"There isn't enough space! {people_in_queue} people in a queue!")
    print(current_state_of_the_lift)
elif people_in_queue == 0 and full_train == True:
    print(current_state_of_the_lift)

