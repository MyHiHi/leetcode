import sys
c = sys.stdin.readlines()
n = int(c[0])
x1 = list(map(int, c[1].split()))
y1 = list(map(int, c[2].split()))
x2 = list(map(int, c[3].split()))
y2 = list(map(int, c[4].split()))
res = 0
for x in x1:
    for y in y1:
        co = 0
        for i in range(n):
            if x >= x1[i] and x < x2[i] and y >= y1[i] and y < x2[i]:
                co += 1
        res = max(co, res)

print(res)
