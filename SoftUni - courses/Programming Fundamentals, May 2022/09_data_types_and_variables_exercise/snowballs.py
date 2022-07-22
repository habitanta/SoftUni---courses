import sys
number_of_snowballs = int(input())
best_snowball = -sys.maxsize
optimal_weight = 0
optimal_time = 0
optimal_quality = 0
for i in range(number_of_snowballs):
    weight = int(input())
    time_for_creation = int(input())
    quality = int(input())
    value_of_ball = (weight // time_for_creation) ** quality
    if value_of_ball > best_snowball:
        best_snowball = value_of_ball
        optimal_weight = weight
        optimal_time = time_for_creation
        optimal_quality = quality
print(f"{optimal_weight} : {optimal_time} = {best_snowball} ({optimal_quality})")
