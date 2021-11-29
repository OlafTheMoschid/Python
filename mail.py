import re


def fun(s):
    pattern = '\w+\-*\d*@[^\W_]+\.\w{,3}$'
    return True if re.fullmatch(pattern, s) else False


def filter_mail(emails):
    return list(sorted(filter(fun, emails)))


def main():
    n = int(input())
    emails = []
    for _ in range(n):
        emails.append(input())
    filtered_emails = filter_mail(emails)
    print('\nOutput:')
    for i in range(len(filtered_emails)):
        print(filtered_emails[i])


if __name__ == '__main__':
    main()
