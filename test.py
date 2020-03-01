S = input().strip()
le = len(S)
res = 0


def isH(i, j, S):
    global res
    while i >= 0 and j < le and S[i] == S[j]:
        print('>>>>>>: ', S[i:j])
        i -= 1
        j += 1
        res += 1


for i in range(le):
    isH(i, i+1, S)
    isH(i, i, S)
print(res)
