from utils import get_neighbours, get_random_neighbours, get_random_state, print_board, calculate_objective, select_best_neighbours


def local_beam_search(n, k):
    state = get_random_state(n)
    print("\n"*(n + 1), end="")
    k_states = get_random_neighbours(state, k)

    while calculate_objective(state):
        print_board(state)
        next_state_canditates = []
        for state in k_states:
            next_state_canditates += get_neighbours(state)

        k_states = select_best_neighbours(next_state_canditates, k)
        state = select_best_neighbours(k_states)[0]

    print_board(state)
    return state
