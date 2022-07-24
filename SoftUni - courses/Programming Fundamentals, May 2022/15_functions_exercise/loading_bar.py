def loading_bar(a):
    percentage_count = "%" * (a // 10)
    time_left = "." * ((100 - a) // 10)
    if a < 100:
        print(f"{a}% [{percentage_count}{time_left}]\nStill loading...")
    elif a == 100:
        print("100% Complete!\n[%%%%%%%%%%]")


number = int(input())
loading_bar(number)



