# https://codeforces.com/contest/1/problem/A

from math import ceil

inp = input()
n, m, a = inp.split()
n = int(n)
m = int(m)
a = int(a)
# print(n, m, a, sep='\n')

odp = ceil(n / a) * ceil(m / a)
print(odp)