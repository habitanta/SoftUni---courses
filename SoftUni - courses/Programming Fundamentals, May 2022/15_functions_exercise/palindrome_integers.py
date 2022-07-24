def palindrome_check(a):
    for digit in a:
        opposite = str(digit)[::-1]
        if digit == int(opposite):
            print("True")
        else:
            print("False")



list_of_digits = [int(s) for s in input().split(",")]

palindrome_check(list_of_digits)