def transform(s):
    result = 0
    for i in s:
        result += ord(i)
        buf = ord(i)
        if i != s[-1]:
            while buf != 0:
                buf //= 10
                result *= 10
    return result
