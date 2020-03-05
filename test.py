from collections import Counter
licensePlate = Counter('steps')
w = "SPPETSS"
c = Counter(w.lower())
v = licensePlate - c
v1 = c-licensePlate
print(licensePlate, Counter(w.lower()), v, v1)
