class PasswordError(BaseException):
    pass


class PasswordLenghtError(PasswordError):
    pass


class PasswordLetterError(PasswordError):
    pass


class PasswordDigitError(PasswordError):
    pass


class PasswordThreeError(PasswordError):
    pass


class PasswordWordsError(PasswordError):
    pass


class PasswordChecker():
    def __init__(self):
        pass

    def lenghtChecker(self, p):
        if len(p) < 9:
            raise PasswordLenghtError(
                "Password lenght must be at least 8 characters")

    def lettersChecker(self, p):
        count1 = 0
        count2 = 0

        for i in p:
            if i.islower():
                count1 += 1
            if i.isupper():
                count2 += 1

        if count1 == 0 or count2 == 0:
            raise PasswordLetterError(
                "Password must contain upper and lower characters")

    def digitsChecker(self, p):
        count1 = 0
        for i in p:
            if i.isdigit():
                count1 += 1

        if count1 == 0:
            raise PasswordDigitError(
                "Password must contain at least one digit")

    def threeChecker(self, p):
        rus = ['йцукенгшщзхъ', 'фывапролджэ', 'ячсмитьбю']
        eng = ['qwertyuiop', 'asdfghjkl', 'zxcvbnm']
        a = p.lower()
        for i in rus:
            for j in range(len(rus) - 2):
                if i[j: j + 3] in a:
                    raise PasswordThreeError(
                        "Password must not contain three continuous characters")

        for i in eng:
            for j in range(len(eng) - 2):
                if i[j: j + 3] in a:
                    raise PasswordThreeError(
                        "Password must not contain three continuous characters")

    def wordListChecker(self, p):
        p.lower()
        wordsList = open('top-9999-words.txt', 'r')
        a = wordsList.readlines()
        wordsList.close()
        for i in a:
            if str(i[:-1]) in p:
                raise PasswordWordsError(
                    "Password must not contain usual words")
