from enum import Enum

class Day:
    def __init__(self, is_gym_opened: bool, is_contest_available: bool):
        self.is_gym_opened = is_gym_opened
        self.is_contest_available = is_contest_available
    
    def __repr__(self):
        activities = (["GYM"] if self.is_gym_opened else []) + (["CODE"] if self.is_contest_available else [])
        return f"{activities}"

class Activity(Enum):
    REST = 1
    GYM = 2
    CODING = 3


def parse_day(encoded_val: int) -> Day:
    return Day(
        is_gym_opened=encoded_val > 1,
        is_contest_available=((encoded_val % 2) == 1),
    )


# (day_index: int, day_activity: Activity) -> min_rest_days: int
cached_results = {}

def calculate_min_rest_days(from_day_index: int, all_days: list[Day], previous_day_activity: Activity):
    if from_day_index >= len(all_days):
        return 0
    
    cache_id = (from_day_index, previous_day_activity)

    if cached_results.get(cache_id) is not None:
        return cached_results.get(cache_id)
    
    # Option I: Rest
    result = 1 + calculate_min_rest_days(from_day_index + 1, all_days, previous_day_activity=Activity.REST)

    current_day = all_days[from_day_index]

    # Option II: Gym
    if previous_day_activity != Activity.GYM and current_day.is_gym_opened:
        result = min(
            result,
            calculate_min_rest_days(from_day_index + 1, all_days, previous_day_activity=Activity.GYM)
        )

    # Option III: Coding
    if previous_day_activity != Activity.CODING and current_day.is_contest_available:
        result = min(
            result,
            calculate_min_rest_days(from_day_index + 1, all_days, previous_day_activity=Activity.CODING)
        )
    
    cached_results[cache_id] = result

    return result


def main():
    # Number of days
    _ = input()

    all_days = [parse_day(int(encoded_str)) for encoded_str in input().split()]

    result = calculate_min_rest_days(
        from_day_index=0,
        all_days=all_days,
        previous_day_activity=Activity.REST,
    )
    print(result)


main()
