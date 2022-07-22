word1 = input()
word2 = input()
current_word = word1
for i in range(len(word1)):
    a = word2[:i + 1:]
    b = word1[i + 1::]
    new_word = a + b
    if new_word != current_word:
        print(new_word)
    current_word = new_word
