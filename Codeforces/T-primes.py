# https://codeforces.com/contest/230/problem/B

from math import isqrt


def is_prime(x):
    if x == 2 or x == 3:
        return True
    if x < 2 or x % 2 == 0 or x % 3 == 0:
        return False
    
    for i in range(6, int(x ** 0.5) + 2, 6):
        if x % (i-1) == 0 or x % (i+1) == 0:
            return False
    return True

def is_t_prime(n):
    a = isqrt(n)
    if a * a == n and is_prime(a):
        return True
    return False


if __name__ == "__main__":
    n = int(input())
    nums = [int(x) for x in input().split()]

    for num in nums:
        if is_t_prime(num):
            print("YES")
        else:
            print("NO")

    # for i in range(1_000):
    #     if (is_t_prime(i)):
    #         print(i)