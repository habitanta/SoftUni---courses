happiness = list(map(int, input().split()))
happiness_improvement_factor = int(input())
real_happiness = list(map(lambda x: x * happiness_improvement_factor, happiness))
average_happiness = sum(real_happiness) / len(real_happiness)
happy_people = list(map(int, filter(lambda x: x >= average_happiness, real_happiness)))

if len(happy_people) >= len(real_happiness) // 2:
    print(f"Score: {len(happy_people)}/{len(happiness)}. Employees are happy!")
else:
    print(f"Score: {len(happy_people)}/{len(happiness)}. Employees are not happy!")