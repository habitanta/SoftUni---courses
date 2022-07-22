age_of_person = int(input())
drink_type = ""
if age_of_person <=14:
    drink_type = "toddy"
elif age_of_person <= 18:
    drink_type = "coke"
elif age_of_person <= 21:
    drink_type = "beer"
else:
    drink_type = "whisky"
print(f"drink {drink_type}")