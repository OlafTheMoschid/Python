from math import sqrt


def roots(a, b, c):
    if isinstance(a, (int, float)) and isinstance(b, (int, float)) and isinstance(c, (int, float)):
        if a == 0:
            return None
        if b == 0 and c <= 0:
            return (-sqrt(-c / a), sqrt(-c / a))
        D = b ** 2 - 4 * a * c
        if D >= 0:
            x1 = (-b - sqrt(D)) / (2 * a)
            x2 = (-b + sqrt(D)) / (2 * a)
            return (x1, x2) if x1 < x2 else (x2, x1)
    return None
