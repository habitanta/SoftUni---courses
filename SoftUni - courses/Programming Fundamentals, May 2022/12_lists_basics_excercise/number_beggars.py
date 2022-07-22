offers_in_str = input().split(", ")
beggars = int(input())
taken_home = []
index = 0
offers_in_int = []
for element in offers_in_str:
    offers_in_int.append(int(element))
while index < beggars:
    sum_for_current_beggar = 0
    for i in range(index, len(offers_in_int), beggars):
        sum_for_current_beggar += offers_in_int[i]
    index += 1
    taken_home.append(sum_for_current_beggar)
print(taken_home)

# ALTERNATE< BUT SLOWER SOLUTION (0.040 s vs 0.090 s)

# list = input().split(", ")
# list1 = []
# list2 = []
# a = int(input())
# for i in range(a):
#     for j in range(i, len(list), a):
#         list1.append(int(list[j]))
#     list2.append(sum(list1))
#     list1.clear()
# print(list2)

