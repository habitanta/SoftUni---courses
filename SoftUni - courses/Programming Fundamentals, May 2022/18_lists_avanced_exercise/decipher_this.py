# MY SOLUTION:

def decipher(a):
    a = [x for x in a]
    number = ""

    for ch in a:
        if ch.isdigit():
            number += ch
        else:
            break

    for ch in number:
        a.remove(ch)

    number = chr(int(number))
    a.insert(0, number)
    a[1], a[-1] = a[-1], a[1]
    return a


secret_message = input().split()
deciphered_message = []

for word in secret_message:
    hidden_word = decipher(word)
    deciphered_message.append("".join(hidden_word))
print(" ".join(deciphered_message))



# N.B. SOLTUION WITH LISTS IS SLOWER THAN SOLUTION WITH ONLY STR\
#     SINCE WHEN WE REMOVE AN ELEMENT FROM THE LIST THE WHOLE LIST IS REINDEXED

# def decipher(a):
#     number = ""
#     for ch in a:
#         if ch.isdigit():
#             number += ch
#         else:
#             break
#     a = a.replace(number, "")
#     print(a)


# BEST SOLUTION IN CLASS BY CHAVDAR:
#
#
# message = input().split()
# deciphered_message = []
#
# for word in message:
#     characters = [ch for ch in word if not ch.isdigit()]
#     nums = [ch for ch in word if ch.isdigit()]
#     ascii_ch = [chr(int("".join(nums)))]
#     current_word = ascii_ch + characters
#     current_word[1], current_word[-1] = current_word[-1], current_word[1]
#     deciphered_message.append(current_word)
# print("".join(deciphered_message))

