
import sys
c = sys.stdin.readlines()
n, k = map(int, c[0].split())
co = 0
if k == 0:
    print(n*n)
else:
    for i in range(k+1, n+1):
        a1 = i-k
        a2 = n//i
        a3 = n % i-k+1
        print('--->: ', a1, a2, a3)
        co += a1*a2+max(a3, 0)
    print(co)
