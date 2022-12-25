# https://codeforces.com/problemset/problem/489/C


# Number of length n can have minimum sum of digits 1:
# 1000...00000
# And maximum 9n:
# 9999...99999

# An average minimal number will be
# 1000..00x99..999
# And maximal
# 9999..99x00..000


if __name__ == "__main__":
    length, summ = [int(x) for x in input().split()]

    if (length, summ) == (1, 0):
        print("0 0")
    elif summ < 1 or summ > 9 * length:
        print("-1 -1")

    else:
        minimal = ""
        remaining = summ - 1
        while remaining > 0:
            digit = str(min(remaining, 9))
            minimal = digit + minimal
            remaining -= int(digit)

        minimal = '0' * (length - len(minimal)) + minimal
        minimal = str(1 + int(minimal[0])) + minimal[1:]

        maximal = ""
        while summ > 0:
            digit = str(min(summ, 9))
            maximal = maximal + digit
            summ -= int(digit)

        maximal = maximal + '0' * (length - len(maximal))

        print(minimal, maximal)
