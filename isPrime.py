# 判断质数
def isPrime(n: int):
    if n == 2:
        return True
    if n <= 1 or n % 2 == 0:
        return False
    for c in range(3, int(n**0.5)+1):
        if n % c == 0:
            return False
    return True

# 得到范围内的所有质数
def getAllPrime(n: int):
    prime = [1 for i in range(n+1)]
    prime[0] = 0
    prime[1] = 0
    for i in range(2, n+1):
        for j in range(i*2, n+1, i):
            prime[j] = 0
    for i in range(n+1):
        if prime[i]:
            print('_____> ', i)


getAllPrime(50)
