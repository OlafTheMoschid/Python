def passwordCheck(s):
    assert len(s) > 8, 'Lenght must be at least 8 characters'

    count1 = 0
    count2 = 0

    for i in s:
        if i.islower():
            count1 += 1
        if i.isupper():
            count2 += 1

    assert count1 != 0 and count2 != 0, 'Password must contain upper and lower characters'

    count1 = 0
    for i in s:
        if i.isdigit():
            count1 += 1

    assert count1 != 0, 'Password must contain at least one digit'

    rusKeyboard = ['йцукенгшщзхъ', 'фывапролджэ', 'ячсмитьбю']
    engKeyboard = ['qwertyuiop', 'asdfghjkl', 'zxcvbnm']
    a = s.lower()

    for i in rusKeyboard:
        for j in range(len(rusKeyboard) - 2):
            assert i[j: j + 3] not in a, 'Password must not contain three continuous characters'

    for i in engKeyboard:
        for j in range(len(engKeyboard) - 2):
            assert i[j: j + 3] not in a, 'Password must not contain three continuous characters'


if passwordCheck(input("Input password: ")):
    print("OK")
else:
    print("ERROR")
