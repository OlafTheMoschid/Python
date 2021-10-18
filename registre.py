import re


class PasswordError(Exception):
    pass


class PasswordLenghtError(PasswordError):
    pass


class PasswordLetterError(PasswordError):
    pass


class PasswordDigitError(PasswordError):
    pass


class PasswordThreeError(PasswordError):
    pass


class NumberError(Exception):
    pass


class FormatError(NumberError):
    pass


class NumberCountError(NumberError):
    pass


class CountryError(NumberError):
    pass


class OperatorError(NumberError):
    pass


class PasswordChecker():
    def __init__(self):
        self.rusKeyboard = ['йцукенгшщзхъ', 'фывапролджэ', 'ячсмитьбю']
        self.engKeyboard = ['qwertyuiop', 'asdfghjkl', 'zxcvbnm']

    def main(self, p):
        self.lenghtChecker(p)
        self.lettersChecker(p)
        self.digitsChecker(p)
        self.threeChecker(p, self.rusKeyboard, self.engKeyboard)
        return True

    def lenghtChecker(self, p):
        if len(p) < 9:
            raise PasswordLenghtError("Lenght must be at least 8 characters")

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

    def threeChecker(self, p, eng, rus):
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


class NumberChecker():
    def __init__(self):
        self.pattern = '^\+?[0-9]-?\(?-?[0-9]-?[0-9]-?[0-9]-?\)?(-?[0-9]-?)*$'
        self.l = [[i for i in range(910, 920)], [i for i in range(980, 990)], [i for i in range(
            920, 940)], [i for i in range(902, 907)], [i for i in range(960, 970)]]

    def main(self, p):
        result = self.countryTransform(p)
        self.formatChecker(self.pattern, p)
        self.counterChecker(result)
        self.coutryChecker(p)
        self.operatorChecker(result, self.l)
        return result

    def formatChecker(self, pattern, p):
        result = re.fullmatch(pattern, p)
        if result is None:
            raise FormatError("Number does not match a format")

    def counterChecker(self, result):
        if len(result) != 12:  # plus and 11 digits
            raise NumberCountError("Number must be 11 characters long")

    def coutryChecker(self, p):
        if not (p[:2] == '+7' or p[0] == '8'):
            raise CountryError("Country code must be +7 or 8")

    def operatorChecker(self, result, l):
        count = 0
        for i in l:
            for j in i:
                if j == int(result[2:5]):
                    count += 1
        if count == 0:
            raise OperatorError(
                "Operator code must match existing operator codes")

    def countryTransform(self, p):
        result = p
        for i in "()-+":
            result = result.replace(i, "")
        return "+7" + result[1:]
