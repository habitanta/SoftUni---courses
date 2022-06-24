number = int(input())
message = ""
for i in range(number):
    code = int(input())
    if code == 88:
        print("Hello")
    elif code == 86:
        print("How are you?")
    elif code < 88 and code != 88 and code != 86:
        print("GREAT!")
    else:
        print("Bye.")
