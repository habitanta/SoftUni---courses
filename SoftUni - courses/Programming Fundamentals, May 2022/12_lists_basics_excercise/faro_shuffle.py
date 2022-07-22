cards = input().split()
faro_shuffles = int(input())
for shuffle in range(faro_shuffles):
    final_deck = []
    middle_of_the_deck = len(cards) // 2
    left = cards[0:middle_of_the_deck]
    right = cards[middle_of_the_deck::]
    for i in range(len(left)):
        final_deck.append(left[i])
        final_deck.append(right[i])
    cards = final_deck
print(cards)