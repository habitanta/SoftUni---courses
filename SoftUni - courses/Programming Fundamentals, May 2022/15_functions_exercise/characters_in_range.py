def ascii_characters_in_between(a, b):
    list_of_characters = []
    for character in range(ord(a) + 1, ord(b)):
        list_of_characters.append(chr(character))
    return " ".join(list_of_characters)


initial_character = input()
end_character = input()
print(ascii_characters_in_between(initial_character, end_character))
