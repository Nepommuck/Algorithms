def usedDigits(n):
    result = [0 for _ in range(10)]
    while n > 0:
        result[n % 10] += 1
        n //= 10
    return result

def sameDigits(a, b):
    return usedDigits(a) == usedDigits(b)

print(
    sameDigits(1255, 5125)
)