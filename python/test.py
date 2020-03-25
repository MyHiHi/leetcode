s = input().strip()
s = s[s.index('"')+1:-1]
dic = input().strip()

dicr = eval("{"+dic[dic.index('"'):]+"}")


def dfs(s, dicr, arr, res):
    if not s:
        print(res)
        arr += [' '.join(res)]
        res = ()
    for w in dicr:
        if s.startswith(w):
            dfs(s[len(w):], dicr, arr, res+(w,))


arr = []
dfs(s, dicr, arr, tuple())
print("["+','.join(arr)+"]")
