command = input()
coffees = 0
while command != "END":
    if command == "coding" or command == "cat" or command == "dog" or command == "movie":
        coffees += 1
    elif command == "CODING" or command == "CAT" or command == "DOG" or command == "MOVIE":
        coffees += 2
    command = input()
if coffees > 5:
    print("You need extra sleep")
else:
    print(coffees)


#alternate solution:

#command = ""
#coffees_needed = 0
#while command.lower() != "end":
#    command = input()
#    if command.lower() == "coding" or command.lower() == "cat" \
#            or command.lower() == "dog" or command.lower() == "movie":
#        if command.islower():
#            coffees needed += 1
#        else: / elif command.isupper():
#        coffees needed += 2
# etc.