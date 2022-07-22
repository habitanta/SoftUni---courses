fires_and_cells = input().split("#")
water = int(input())
total_effort = 0
total_fire = 0
final_value_list = []
for i in fires_and_cells:
    element_list = i.split(" = ")
    fire_type = element_list[0]
    value = int(element_list[1])
    if "High" in i and (81 > value or value > 125):
        continue
    elif "Medium" in i and (51 > value or value > 80):
        continue
    elif "Low" in i and (1 > value or value > 50):
        continue
    elif water < value:
        continue
    else:
        water -= value
        effort = 25 * value / 100
        total_effort += effort
        final_value_list.append(value)
        total_fire += int(value)
print("Cells:")
for element in final_value_list:
    print(f"- {element}")
print(f"Effort: {total_effort:.2f}")
print(f"Total Fire: {total_fire}")






