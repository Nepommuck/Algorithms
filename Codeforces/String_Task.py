# https://codeforces.com/problemset/problem/118/A

from functools import reduce


flat_map = lambda f, xs: reduce(lambda a, b: a + b, map(f, xs))

VOWELS = list("AOYEUI")
is_vowel = lambda letter: letter.isalpha() and letter.upper() in VOWELS
is_consonant = lambda letter: letter.isalpha() and not is_vowel(letter)


def transform(letter):
    if is_vowel(letter):
        return []
    return ['.', letter.lower()]


def main():
    list_to_string = lambda l: "".join(l)

    word = input()
    # result = "".join(flat_map(transform, list(word)))
    result = list_to_string(flat_map(transform, list(word)))
    print(result)


main()
