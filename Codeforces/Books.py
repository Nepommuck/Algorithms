def solve(t, books):
    score = 0
    best_score = 0
    start, end = 0, 0
    time_used = 0

    while end < len(books):
        # We can read next book
        if time_used + books[end] <= t:
            score += 1
            time_used += books[end]
            end += 1

        # Not enough time
        else:
            score -= 1
            time_used -= books[start]
            start += 1

        best_score = max(score, best_score)

    return best_score


def main():
    _, t = map(lambda s: int(s), input().split())
    books = list(map(lambda s: int(s), input().split()))

    print(solve(t, books))


main()
