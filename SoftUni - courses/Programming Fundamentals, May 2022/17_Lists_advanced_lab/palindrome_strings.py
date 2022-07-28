words = input().split()
palindromes = [x for x in words if x == x[::-1]]
print(palindromes)
search_for_palindrome = input()
number = palindromes.count(search_for_palindrome)
print(f"Found palindrome {number} times")

