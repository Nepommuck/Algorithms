import math
from collections import deque


def get_depth(num, goal):
    stack = deque()
    stack.append(
        (num, 0)
    )
    best = math.inf

    while stack:
        el, d = stack.pop()
        if d < best:
            if el == goal:
                best = d
            else:
                stack.append(
                    (el - 1, d + 1)
                )
                if el < goal:
                    stack.append(
                        (2 * el, d + 1)
                    )
    return best


if __name__ == "__main__":
    number, goal = [int(x) for x in input().split()]
    print(get_depth(number, goal))

