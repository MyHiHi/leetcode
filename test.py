def isPowerOfThree(n: int) -> bool:
    if not n:
        return False
    while n:
        if n == 1 or n == 2:
            return False
        n %= 3
        print("n: ", n)
    return True


print(isPowerOfThree(45))
