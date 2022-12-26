# https://codeforces.com/problemset/problem/1774/B
# UNSOLVED

def possible_to_fill(n, k, colors):
    tape = [None for _ in range(n)]
    for i in range(len(colors)):
        j = 0
        while colors[i] > 0:
            if j >= n:
                return False
            while tape[j] is not None:
                j += 1
                if j >= n:
                    return False

            tape[j] = i
            colors[i] -= 1
            j += k

    return True


tests = int(input())
for _ in range(tests):
    n, _, k = [int(x) for x in input().split()]
    colors = [int(x) for x in input().split()]
    colors.sort()

    print("YES" if possible_to_fill(n, k, colors) else "NO")
