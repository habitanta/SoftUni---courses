animals = input().split(" ")
number = int(input())
animals_final = []
for n in range(0, len(animals)):
    animals[n] = int(animals[n])
for i in range(number):
    min_number = min(animals)
    animals.remove(min_number)
for m in animals:
    animals_final.append(str(m))

print(", ".join(animals_final))
