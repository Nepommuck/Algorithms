def readN(mask, n):
    for _ in range(n):
        mask //= 2
    return True if mask % 2 == 1 else False


def getMask(num, base):
    mask = 0

    while num > 0:
        dig = num % base
        if not readN(mask, dig):
            mask += 2 ** dig
        num //= base

    return mask

def masksWithDifferentDigits(a, b):
    while a > 0 and b > 0:
        if a % 2 == 1 and b % 2 == 1:
            return False
        a //= 2
        b //= 2
    return True


if __name__ == "__main__":
    a = int(input())
    b = int(input())
    # a = 123
    # b = 522

    answer = None
    for base in range(2, 16+1):

        maskA = getMask(a, base)
        maskB = getMask(b, base)
                
        if masksWithDifferentDigits(maskA, maskB):
            answer = base
            break

    if answer is not None:
        print("Baza to:", base)
    else:
        print("Nie ma takiej bazy")
