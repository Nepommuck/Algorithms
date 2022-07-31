def fun(tab, i, pom):
    if i >= len(tab):
        return 0

    if pom[i] is None:
        pom[i] = max(
            i * tab[i] + fun(tab, i+2, pom),
            fun(tab, i+1, pom)
        )
    return pom[i]


if __name__ == "__main__":
    n = int(input())
    nums = [int(x) for x in input().split()]

    mx = max(nums)
    counter = [0 for _ in range(mx+1)]
    for num in nums:
        counter[num] += 1

    pom = [None for _ in range(mx+1)]

    print(fun(counter, 1, pom))