words = input().split()
even_sized_words = [x for x in words if len(x) % 2 == 0]
print("\n".join(even_sized_words))