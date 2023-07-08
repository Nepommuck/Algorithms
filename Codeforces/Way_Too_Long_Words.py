# https://codeforces.com/problemset/problem/71/A

MIN_LENGTH_TO_ABBRERIATE = 11


def abbreviation(word):
    if len(word) < MIN_LENGTH_TO_ABBRERIATE:
        return word
    return word[0] + str(len(word) - 2) + word[-1]

def main():
    number_of_words = int(input())
    words = [input() for _ in range(number_of_words)]
    result = list(map(abbreviation, words))
    for word in result:
        print(word)


main()
