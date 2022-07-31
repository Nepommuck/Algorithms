name = input()
n = ord('z') - ord('a') + 1
counter = [0 for _ in range(n)]

for let in name:
    counter[ord(let) - ord('a')] += 1

odp = 0
for c in counter:
    if c > 0:
        odp += 1

# Female
if odp % 2 == 0:
    print('CHAT WITH HER!')
# Male 
else:
    print('IGNORE HIM!')