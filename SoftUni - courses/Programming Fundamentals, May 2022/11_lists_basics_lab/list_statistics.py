number = int(input())
positives = []
negatives = []
count_positives = 0
sum_of_negatives = 0
for i in range(number):
    data = int(input())
    if data >= 0:
        positives += [data]
        count_positives += 1
    else:
        negatives += [data]
        sum_of_negatives += data
print(positives)
print(negatives)
number = int(input())
positives = []
negatives = []
count_positives = 0
sum_of_negatives = 0
for i in range(number):
    data = int(input())
    if data >= 0:
        positives += [data]
        count_positives += 1
    else:
        negatives += [data]
        sum_of_negatives += data
print(positives)
print(negatives)
print(f"Count of positives: {count_positives}")
print(f"Sum of negatives: {sum_of_negatives}")

# print(f"Count of positives: {len(positives)}")
# print(f"Sum of negatives: {sum(negatives)}")

