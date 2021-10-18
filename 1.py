def passwordCheck(s):
    if len(s) < 8:
        return False

    count1 = 0
    count2 = 0

    for i in s:
        if i.islower():
            count1 += 1
        if i.isupper():
            count2 += 1

    if count1 == 0 and count2 == 0:
        return False

    count1 = 0
    for i in s:
        if i.isdigit():
            count1 += 1

    if count1 == 0:
        return False

    rusKeyboard = ['йцукенгшщзхъ', 'фывапролджэ', 'ячсмитьбю']
    engKeyboard = ['qwertyuiop', 'asdfghjkl', 'zxcvbnm']
    a = s.lower()

    for i in rusKeyboard:
        for j in range(len(rusKeyboard) - 2):
            if i[j: j + 3] in a:
                return False

    for i in engKeyboard:
        for j in range(len(engKeyboard) - 2):
            if i[j: j + 3] in a:
                return False

    return True


if passwordCheck(input("Input password: ")):
    print("OK")
else:
    print("ERROR")
