p = '["a","ab","abc","cd","bcd","abcd"]'
l = eval(p)
l = sorted(l, key=lambda x: len(x), reverse=True)
print(l)
