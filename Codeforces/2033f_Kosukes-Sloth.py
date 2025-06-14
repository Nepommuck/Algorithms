class FibonacciStepper:
    def __init__(self, k):
        self.k = k
        self.current = 1
        self.prev = 1
        self.index = 2
    
    def step(self):
        self.index += 1

        self.current, self.prev = (self.current + self.prev) % self.k, self.current


class SolutionParams:
    def __init__(self, pre_cycle_null_distances: list, loop_start_index: int, loop_distances: list):
        self.simple_solution = None

        self.pre_cycle_null_distances = pre_cycle_null_distances
        self.loop_start_index = loop_start_index
        self.loop_distances = loop_distances

        self.pre_cycle_nulls_count = len(pre_cycle_null_distances)
        self.nulls_in_loop = len(loop_distances)
        self.loop_total_distance = loop_distances[-1]


class SimpleSolution:
    def __init__(self, result):
        self.simple_solution = result


def solve(n: int, k: int) -> SolutionParams | SimpleSolution:
    fib_stepper = FibonacciStepper(k)

    # prev -> index
    known_nulls = {}
    nulls_encountered = []

    while True:
        if fib_stepper.current == 0:
            if known_nulls.get(fib_stepper.prev) is None:
                known_nulls[fib_stepper.prev] = fib_stepper.index
                nulls_encountered.append(fib_stepper.prev)

                if len(nulls_encountered) == n:
                    return SimpleSolution(fib_stepper.index)
            
            # Cycle found
            else:
                pre_cycle_nulls = []
                cycle_nulls = []
                
                for i, prev_value in enumerate(nulls_encountered):
                    if prev_value == fib_stepper.prev:
                        pre_cycle_nulls = nulls_encountered[: i]
                        cycle_nulls = nulls_encountered[(i + 1) :]
                        break
                
                loop_start_index = known_nulls[fib_stepper.prev]
                loop_indices = [known_nulls[null] for null in cycle_nulls] + [fib_stepper.index]
            

                return SolutionParams(
                    pre_cycle_null_distances=[known_nulls[null] for null in pre_cycle_nulls],
                    loop_start_index=loop_start_index,
                    loop_distances=[index - loop_start_index for index in loop_indices],
                )
        
        fib_stepper.step()


def calculate(solution: SolutionParams, n: int, k: int) -> int:
    n = n - (solution.pre_cycle_nulls_count + 1)

    full_loops = n // solution.nulls_in_loop
    additional_steps = n - full_loops * solution.nulls_in_loop

    return solution.loop_start_index + full_loops * solution.loop_total_distance + solution.loop_distances[additional_steps]


def answer(n: int, k: int) -> int:
    if k == 1:
        return n
    
    solution = solve(n, k)
    if solution.simple_solution is not None:
        return solution.simple_solution
    
    return calculate(solution, n, k)


def main():
    number_of_testcases = int(input())

    for _ in range(number_of_testcases):
        n, k = [int(value) for value in input().split()]
        print(answer(n, k))


main()
