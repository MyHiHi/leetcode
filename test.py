from collections import Counter
p = "aaabccccccddeee"+"0"

# p = input().strip()
res = ""
le = len(p)
k, v = p[0], 1
for i in range(1, le):
    s = p[i]
    if s != k:
        res += str(v)+k
        k = s
        v = 1
    else:
        v += 1
print(res)
