def isSubsequence(seq, b):
    l = len(b)
    if len(seq) < l:
        return False
    return seq[:l] == b or isSubsequence(seq[1:], b)

def getLongestReverse(seq, chopped, n):
    if len(chopped) < n:
        return getLongestReverse(seq, seq, n-1)
    if isSubsequence(seq, chopped[:n][::-1]):
        return n
    return getLongestReverse(seq, chopped[1:], n)

def longestReverse(seq):
    return getLongestReverse(seq, seq, len(seq))


a = [2, 9, 3, 1, 7, 11, 9, 6, 7, 7, 1, 3, 9, 12, 15]
print(
    longestReverse(a)
)
