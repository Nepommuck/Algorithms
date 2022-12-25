# https://codeforces.com/contest/1773/problem/E


if __name__ == "__main__":
    n = int(input())
    arr = []

    id = 0
    for i in range(n):
        nums = [int(x) for x in input().split()[1:]]
        id += 1

        # Each block is added to the array together with number of the tower
        # (if text number in tower is smaller than previous we make a new tower out of that)
        arr.append((nums[0], id))
        for j in range(1, len(nums)):
            if nums[j-1] > nums[j]:
                id += 1
            arr.append((nums[j], id))

        id += 1

    arr.sort()

    current = 0
    for i in range(1, len(arr)):
        # If neighbouring ids are different, than we need to further divide the tower
        if arr[i][1] != arr[i-1][1]:
            current += 1

    # Splits
    print(current + 1 - n, end=' ')

    # Combines
    print(current)
