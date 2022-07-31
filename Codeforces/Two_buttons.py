# https://codeforces.com/contest/520/problem/B


def get_depth(num, goal):
    steps = 0
    while num != goal:
        if goal < num or goal % 2 == 1:
            goal += 1
        else:
            goal //= 2
        steps += 1

    return steps


if __name__ == "__main__":
    number, goal = [int(x) for x in input().split()]
    print(get_depth(number, goal))

