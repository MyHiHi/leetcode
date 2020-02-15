n, k = list(map(int, input().strip().split()))
tower = []
for i, v in enumerate(list(map(int, input().strip().split()))):
    tower += [[v, i+1]]
tower = sorted(tower, key=lambda x: x[0])
res = []
t = 0
while tower[-1][0]-tower[0][0] > 0 and k > 0:
    tower[-1][0] -= 1
    tower[0][0] += 1
    res += [str(tower[-1][1])+" "+str(tower[0][1])]
    tower = sorted(tower, key=lambda x: x[0])
    t += 1
    k -= 1
res = [str(tower[-1][0]-tower[0][0])+" "+str(t)]+res
for k in res:
    print(k)
