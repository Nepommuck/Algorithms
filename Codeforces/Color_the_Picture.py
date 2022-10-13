# https://codeforces.com/contest/1710/problem/A


def possible_to_color(n, m, colors):
    return try_cover(n, m, colors) or try_cover(m, n, colors)


def try_cover(rows, cols, colors):
    covered = 0
    used_big = False
    for color in colors:
        akt = color // rows
        if akt >= 2:
            covered += akt
        if akt >= 3:
            used_big = True

        if covered == cols or covered > cols and used_big:
            return True
    return False


if __name__ == "__main__":
    tests = int(input())

    for _ in range(tests):
        # Get input
        n, m, k = [int(x) for x in input().split()]
        a = [int(x) for x in input().split()]

        print('Yes' if possible_to_color(n, m, a) else 'No')
