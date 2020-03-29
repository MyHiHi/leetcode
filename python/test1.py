def quick(lis): return lis if len(lis) < 2 else quick([
    i for i in lis[1:] if i <= lis[0]])+[lis[0]]+quick([p for p in lis[1:] if p > lis[0]])


print(quick([1, 5, 3, 2, 5, 1, 4, 4, 4, 23, 12, 56, 4]))
