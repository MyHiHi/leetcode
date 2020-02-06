p = ["a1 9 2 3 1", "g1 act car", "zo4 4 7", "ab1 off key dog", "a8 act zoo"]


def r(log):
    _id, rest = log.split(" ", 1)
    return (0, rest, _id) if rest[0].isalpha() else (1,)


ry = sorted(p, key=r)
print(ry)
