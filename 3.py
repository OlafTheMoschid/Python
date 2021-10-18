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


class PasswordChecker():
    def __init__(self):
        self.rusKeyboard = ['йцукенгшщзхъ', 'фывапролджэ', 'ячсмитьбю']
        self.engKeyboard = ['qwertyuiop', 'asdfghjkl', 'zxcvbnm']

    def main(self, p):
        self.lenghtChecker(p)
        self.lettersChecker(p)
        self.digitsChecker(p)
        self.threeChecker(p, self.rusKeyboard, self.engKeyboard)

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


pw = input("Input password: ")
password = PasswordChecker()
try:
    password.main(pw)
    print("OK")
except PasswordError as e:
    print(e.args[0])
