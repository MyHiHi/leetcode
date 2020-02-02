# N, M = map(int, input().split())
# job = {}
# res = []
# for _ in range(N):
#     a, b = map(int, input().split())
#     job[b] = a
# job = sorted(job.items(), key=lambda x: x[0], reverse=True)

# ability = map(int, input().split())
# ab = dict(zip(range(M), ability))

# ability = sorted(ab.items(), key=lambda x: x[1], reverse=True)
# res = {}
# start = 0
# k = 0
# print("ability:", ability)
# print("job:", job)
# for index, ab in ability:
#     for p, d in job[start:]:
#         if ab >= d:
#             res[index] = p
#             start = k
#             break
#         k += 1
# print(res)
# res = sorted(res.items(), key=lambda x: x[0])
# for _, k in res:
#     print(k)


# N, M = map(int, input().split())
# job_money = {}
# for i in range(N):
#     a, b = map(int, input().split())
#     job_money[a] = b
# c = map(int, input().split())
# index = []
# for v in c:
#     index += [v]
#     job_money[v] = 0 if v not in job_money else job_money[v]
# job_money = sorted(job_money.items(), key=lambda x: x[0])
# mx = 0
# res = {}
# for i, k in job_money:
#     mx = max(mx, k)
#     res[i] = mx

# for v in index:
#     print(res[v])

import sys
lines = sys.stdin.readlines()
lines = [l.strip().split() for l in lines if l.strip()]
N, M = map(int, lines[0])
job_money = {}
for i in lines[1:-1]:
    a, b = map(int, i)
    job_money[a] = b
c = map(int, lines[-1])
index = []
for v in c:
    index += [v]
    job_money[v] = 0 if v not in job_money else job_money[v]
job_money = sorted(job_money.items(), key=lambda x: x[0])
mx = 0
res = {}
for i, k in job_money:
    mx = max(mx, k)
    res[i] = mx

for v in index:
    print(res[v])
