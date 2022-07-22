year = int(input())
happy_year_condition = False
while not happy_year_condition:
    year += 1
    set_year = set(())

    for i in range(len(str(year))):
        set_year.add(str(year)[i])

    happy_year_condition = len(set_year) == len(str(year))
print(year)

# x = set() - used to initiate a set, also works with (()), but x = {} initiate a dictionary
# and only x=() initiate a tuple.
# .add - adds to that set
