number = int(input())
word = input()
list_of_words = []
proper_list = []
for i in range(number):
    current_word = input()
    list_of_words += [current_word]
    if word in current_word:
        proper_list += [current_word]
print(list_of_words)
print(proper_list)