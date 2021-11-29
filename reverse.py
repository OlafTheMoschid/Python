def reverse(s):
    if type(s) != str:
        raise TypeError(f'Expected str, got {type(s)}')
    return s[::-1]
