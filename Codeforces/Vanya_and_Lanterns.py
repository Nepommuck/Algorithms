# https://codeforces.com/problemset/problem/492/B


if __name__ == "__main__":
    n, l = [int(x) for x in input().split()]
    coords = [int(x) for x in input().split()]
    coords.sort()

    res = max(coords[0], l - coords[-1])
    for i in range(n-1):
        res = max(
            res,
            (coords[i+1] - coords[i]) / 2
        )
    print(res)
