from bisect import bisect
p = [1, 2, 3, 4, 5]


def binary_search(p, k):
    l, r = 0, len(p)-1
    while l < r:
        n = (l+r) >> 1
        if p[n] <= k:
            l=n+1
        else:
            r=n
    return l


k = binary_search(p, 2)
print(k)
