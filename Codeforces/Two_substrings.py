# https://codeforces.com/problemset/problem/550/A

def solve(string):
    l = len(string)
    i = 1
    substrings = ["AB", "BA"]
    for substr in substrings:
        if substr not in string:
            return False

    while i < l:
        substring = string[i-1:i+1]
        for substr1, substr2 in zip(substrings, substrings[::-1]):
            if substring == substr1 and substr2 in string[i+1:]:
                return True
        i += 1
    return False


def main():
    string = input()
    print("YES" if solve(string) else "NO")

main()
