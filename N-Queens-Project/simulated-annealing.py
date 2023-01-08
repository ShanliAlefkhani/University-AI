import math
import decimal
import random

from utils import get_random_neighbours, get_random_state, print_board, calculate_objective


if __name__ == "__main__":
    n = int(input())
    temperature = 4000
    sch = 0.99
    state = get_random_state(n)
    print("\n"*(n + 1), end="")

    while True:
        print_board(state)
        temperature *= sch
        next_state = get_random_neighbours(state.copy())[0]
        dw = calculate_objective(state) - calculate_objective(next_state)
        exp = decimal.Decimal(decimal.Decimal(math.e) ** (decimal.Decimal(dw) * decimal.Decimal(temperature)))

        if dw > 0 or random.uniform(0, 1) < exp:
            state = next_state

        if calculate_objective(state) == 0:
            print_board(state)
            break
