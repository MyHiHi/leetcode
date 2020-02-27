n1, n2 = list(map(int,input().strip().split(','))), list(map(int,input().strip().split(',')))
res = []
if n1[0] > n2[-1]:
    res += n2+n1
elif n1[-1] < n2[0]:
    res += n1+n2
else:
    l, r = 0, 0
    l1, l2 = len(n1), len(n2)
    while l < l1 and r < l2:
        k1, k2 = n1[l], n2[r];
        if k1 < k2:
            res += [k1]
            l += 1
        elif k1 > k2:
            res += [k2]
            r += 1
        else:
            res += [k1, k2]
            l += 1
            r += 1

    if l < l1:
        res += n1[l:]
    elif r < l2:
        res += n2[r:]
print(','.join(map(str,res)))
try:
    pass
except expression as identifier:
    pass