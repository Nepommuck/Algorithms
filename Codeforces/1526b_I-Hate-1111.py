def get_111(number_of_digits: int) -> int:
    return int("".join(['1' for _ in range(number_of_digits)]))

# (number: int, max_len_111: int) -> bool
cached_results = {}

def can_be_a_sum(number: int, max_len_111: int) -> int:
    if number == 0:
        return True
    
    if max_len_111 <= 1 or number < 11:
        return False
    
    if cached_results.get((number, max_len_111)) is not None:
        return cached_results.get((number, max_len_111))
    
    cached_results[(number, max_len_111)] = \
        can_be_a_sum(number - get_111(max_len_111), max_len_111) or \
        can_be_a_sum(number, max_len_111 - 1)

    return cached_results[(number, max_len_111)]


def is_sum_of_111(number: int) -> bool:
    return can_be_a_sum(number, max_len_111=len(str(number)))


def main():
    number_of_test_cases = int(input())

    inputs = []
    for _ in range(number_of_test_cases):
        number = int(input())
        print("YES" if is_sum_of_111(number) else "NO")

main()
