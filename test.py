# n, m, k = list(map(int, input().strip().split()))
# arr = ['a']*n+['z']*m


# def rev(arr, s, e, res):
#     if s == e:
#         res.add(''.join(map(str,arr[:])))
#     else:
#         for i in range(s, e):
#             arr[i], arr[s] = arr[s], arr[i]
#             rev(arr, s+1, e, res)
#             arr[i], arr[s] = arr[s], arr[i]


# res = set()
# rev(arr, 0, len(arr), res)
# print(res)
# list(res).sort()
# # res.sort()2 2 6
# print(res, len(res))
# # print(''.join(map(str, res[k])))


def bitwiseComplement(N: int) -> int:
    c = bin(N)[2:]
    p = ""
    for i in c:
        p += '1' if i == '0' else '0'
    print(c, p)
    return int(p, 2)


print(bitwiseComplement(10))
