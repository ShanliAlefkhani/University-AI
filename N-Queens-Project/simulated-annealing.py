import math
import decimal
from random import randint, uniform

from utils import print_board, calculate_objective


def get_neighbour(state):
    op_state = state.copy()
    op_state[randint(0, len(state) - 1)] = randint(0, len(state) - 1)
    return op_state

if __name__ == "__main__":
    n = int(input())
    temperature = 4000
    sch = 0.99
    state = [randint(0, n - 1) for _ in range(n)]
    print("\n"*(n + 1), end="")

    while True:
        print_board(state)
        temperature *= sch
        next_state = get_neighbour(state.copy())
        dw = calculate_objective(state) - calculate_objective(next_state)
        exp = decimal.Decimal(decimal.Decimal(math.e) ** (decimal.Decimal(dw) * decimal.Decimal(temperature)))

        if dw > 0 or uniform(0, 1) < exp:
            state = next_state

        if calculate_objective(state) == 0:
            print_board(state)
            break
