characters = input().split(", ")
dict = {characters[i] : ord(characters[i]) for i in range(0, len(characters))}
print(dict)
