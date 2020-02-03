import sys
lines = sys.stdin.readlines()
lines = [line.strip() for line in lines if line.strip()]
l, r = map(int, lines[0].split())


def get(m):
    su = m//3*2
    if m % 3 == 2:
      su += 1
      return su 
    return su


print(get(r)-get(l-1))
