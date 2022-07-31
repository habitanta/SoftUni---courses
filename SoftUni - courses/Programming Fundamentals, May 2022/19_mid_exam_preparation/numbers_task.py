number = list(map(int,input().split()))
average_sum = sum(number) // len(number)
top_5 = [x for x in number if x > average_sum]
top_5.sort(reverse=True)
top_5 = [top_5[x] for x in range(0, len(top_5)) if x <= 4]
if top_5 == []:
    print("No")
else:
    print(" ".join(map(str, top_5)))


