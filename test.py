from functools import cmp_to_key


def cmp(a, b):
    if a<b:
      return -1;
    else:
      return 1


p = [1, 2, 3, 1, 57, 3, 2, 100]
p=sorted(p,key=cmp_to_key(cmp))
print(p)
