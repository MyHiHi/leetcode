def isPowerOfFour(num: int) -> bool:
    while num != 1:
        print("*********:", num)
        if num < 1:
            break
        num /= 4
    else:
        print("&&&&&", num)
        return False
    return True


c = isPowerOfFour(16)
print(c)
