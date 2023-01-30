from utils import calculate_objective, get_neighbours, print_board, select_best_neighbours, get_random_state


def hill_climbing(n):
	state = get_random_state(n)
	print("\n"*(n + 1), end="")

	while True:
		print_board(state)
		next_state = select_best_neighbours(get_neighbours(state.copy()))[0]

		if calculate_objective(state) <= calculate_objective(next_state):
			break
		state = next_state
