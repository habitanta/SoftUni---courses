synonyms_dict = {}
number_of_words = int(input())
for word in range(0,number_of_words):
    new_word = input()
    synonym = input()
    if new_word in synonyms_dict:
        synonyms_dict[new_word].append(synonym)
    else:
        synonyms_dict[new_word] = [synonym]

for key, value in synonyms_dict.items():
    unpacked_value = ", ".join(value)
    print(f"{key} - {unpacked_value}")