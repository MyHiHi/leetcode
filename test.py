def run(s: str):
    le = len(s)
    # start 用来获取表达式第一个数字
    start, end = True, 1
    res = 0
    while end < le:
        if s[end] == '/':
            if start:
                res = int(s[:end])
            start = False
            end += 1
            k = end
            while end < le and s[end].isdigit():
                end += 1
            res /= int(s[k:end])
        elif s[end] == '*':
            if start:
                res = int(s[:end])
            start = False
            end += 1
            k = end
            while end < le and s[end].isdigit():
                end += 1
            res *= int(s[k:end])
        else:
            end += 1
    return res


s = "12*3/2*5/6"
print(run(s))
