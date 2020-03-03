from collections import Counter
arr = [1, 2, 2, 6, 6, 6, 6, 7, 10]
p = Counter(arr).most_common(2)
print(p)
