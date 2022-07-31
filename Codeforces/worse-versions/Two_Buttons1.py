from math import log2, floor


def left(n):
    return 2*n + 1

def right(n):
    return 2*n + 2

def parent(n):
    return (n - 1) // 2

def level(n):
    return floor(log2(n+1))


number, goal = [int(x) for x in input().split()]

arr = [number]
i = 0
while arr[i] != goal:
    i += 1
    if i % 2 == 1:
        n_el = 2 * arr[parent(i)]
    else:
        n_el = arr[parent(i)] - 1
    arr.append(n_el)

print(level(i))
# print(arr)
