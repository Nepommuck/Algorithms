n = int(input())
nums = [int(x) for x in input().split()]

counter = [0, 0]
for i in range(3):
    counter[nums[i] % 2] += 1

# We are searching for an odd number
if counter[0] >= 2:
    desired = 1
# We are searching for an even number
else:
    desired = 0

for i in range(n):
    if nums[i] % 2 == desired:
        print(i + 1)
        break
