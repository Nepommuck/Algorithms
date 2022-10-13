# https://codeforces.com/contest/1711/problem/A

if __name__ == "__main__":
    tests = int(input())
    for _ in range(tests):        
        k = int(input())

        for i in range(2, k+1):
            print(i, end=' ')
        print('1')
