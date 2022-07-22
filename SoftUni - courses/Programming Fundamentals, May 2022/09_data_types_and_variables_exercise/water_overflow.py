n = int(input())
litres_in_tank = 0
for i in range(n):
    litres = int(input())
    if (litres_in_tank + litres) > 255:
        print("Insufficient capacity!")
        continue
    else:
       litres_in_tank += litres
print(litres_in_tank)


