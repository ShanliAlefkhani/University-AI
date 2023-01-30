import math
import decimal
import random

from utils import get_random_neighbours, get_random_state, print_board, calculate_objective


def simulated_annealing(n):
    temperature = 4000
    schedule = 0.99
    state = get_random_state(n)
    print("\n"*(n + 1), end="")

    while calculate_objective(state) and temperature > 0.2:
        print_board(state)
        temperature *= schedule
        next_state = get_random_neighbours(state.copy())[0]
        e = calculate_objective(state) - calculate_objective(next_state)
        exp = decimal.Decimal(decimal.Decimal(math.e) ** (decimal.Decimal(e) * decimal.Decimal(temperature)))

        if e > 0 or random.uniform(0, 1) < exp:
            state = next_state

    print_board(state)
    return state
