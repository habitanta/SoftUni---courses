word = input()
while word != "End":
    double_word = ""
    if word == "SoftUni":
        continue
    else:
        for i in word:
            double_word += i * 2
        print(double_word)
        word = input()


