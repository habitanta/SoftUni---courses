def check_chairs(number_of_rooms):
    total_free_chairs = 0
    needed_chairs = 0
    for room in range(1, number_of_rooms + 1):
        free_chairs, visitors = input().split()
        diff = len(free_chairs) - int(visitors)
        if diff >= 0:
            total_free_chairs += diff
        else:
            needed_chairs +=abs(diff)
            print(f"{abs(diff)} more chairs needed in room {room}")

    return total_free_chairs, needed_chairs


number_of_rooms = int(input())
total_free_chairs, needed_chairs = check_chairs(number_of_rooms)
if total_free_chairs >= needed_chairs:
    print(f"Game On, {total_free_chairs} free chairs left")


# MY SOLUTION:
#
# def subtraction(a,b):
#     return a - b
#
#
# number_of_rooms = int(input())
# total_available_chairs = 0
# condition = True
#
# for room in range(0,number_of_rooms):
#     info = input().split()
#     chairs_available = len(info[0])
#     visitors = int(info[1])
#     diff = abs(subtraction(visitors, chairs_available))
#     if chairs_available < visitors:
#         print(f"{diff} more chairs needed in room {room + 1}")
#         condition = False
#     else:
#         total_available_chairs += diff
#
# if condition == True:
#     print(f"Game On, {total_available_chairs} free chairs left")

