# https://codeforces.com/problemset/problem/1711/B

import math


def party(unhapp, friends, counter):        
    n = len(unhapp)
    best = math.inf

    # Try removing a single person with odd number of friends
    for i in range(n):
        if counter[i] % 2 == 1:
            best = min(best, unhapp[i])
    
    # Try removing a pair of friends each with an even number of friends
    for v, k in friends:
        if counter[v] % 2 == 0 and counter[k] % 2 == 0:
            best = min(best, unhapp[v] + unhapp[k])
    
    return best


if __name__ == "__main__":
    tests = int(input())

    for _ in range(tests):
        # Get input
        n, m = [int(x) for x in input().split()]
        a = [int(x) for x in input().split()]
        edges = []
        counter = [0 for _ in range(n)]

        for _ in range(m):
            v, k = [int(x)-1 for x in input().split()]
            counter[v] += 1
            counter[k] += 1
            edges.append((v, k))
    
        print(party(a, edges, counter) if m % 2 == 1 else 0)
