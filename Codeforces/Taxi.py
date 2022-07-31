# https://codeforces.com/contest/158/problem/B

from math import ceil


n = int(input())
st = input()
groups = st.split()
counter = [0 for _ in range(4)]
cars = 0

for group in groups:
    k = int(group)
    # Groups of 4 need own car
    if k == 4:
        cars += 1
    else:
        counter[k] += 1

# Get 3 and 1 groups together
cars += counter[3]
counter[1] = max(counter[1] - counter[3], 0)
counter[3] = 0

# Get groups of 2
cars += counter[2] // 2
counter[2] %= 2

children_left = 1 * counter[1] + 2 * counter[2]
cars += ceil(children_left / 4)

print(cars)
