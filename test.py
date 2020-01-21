def judgeSquareSum(c: int) -> bool:
    for i in range(1, int(c**0.5)+1):
        r = (c-i*i)**0.5
        k = int(r)
        if r**2 == k**2:
            return True
    return False


p = judgeSquareSum(3)
print(p)
