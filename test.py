def hammingWeight(n: int):
    return len(list(filter(lambda s: s == "1", str(n))))


n = "00000000000000000000000000001011"

print(hammingWeight(n))
