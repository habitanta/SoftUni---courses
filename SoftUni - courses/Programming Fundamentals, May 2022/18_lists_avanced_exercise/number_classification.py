def is_number_positive(a):
    a = ", ".join(str(x) for x in a if x >= 0)
    return a

def is_number_negative(a):
    a = ", ".join(str(x) for x in a if x < 0)
    return a

def is_number_even(a):
    a = ", ".join(str(x) for x in a if x % 2 == 0)
    return a

def is_number_odd(a):
    a = ", ".join(str(x) for x in a if x % 2 != 0)

    return a

numbers = [int(x) for x in input().split(", ")]
print(f"Positive: {is_number_positive(numbers)}")
print(f"Negative: {is_number_negative(numbers)}")
print(f"Even: {is_number_even(numbers)}")
print(f"Odd: {is_number_odd(numbers)}")