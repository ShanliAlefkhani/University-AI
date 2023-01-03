from random import randint
from utils import calculate_objective, print_board


def get_neighbour(state):
	op_state = state.copy()
	op_obj = calculate_objective(op_state)

	for i in range(len(state)):
		for j in range(len(state)):
			if j != state[i]:
				neighbour_state = state.copy()
				neighbour_state[i] = j
				neighbour_obj = calculate_objective(neighbour_state)

				if neighbour_obj <= op_obj:
					op_obj = neighbour_obj
					op_state = neighbour_state.copy()
	return op_state


if __name__ == "__main__":
	n = int(input())
	state = [randint(0, n - 1) for _ in range(n)]
	print("\n"*(n + 1), end="")
	while True:
		next_state = get_neighbour(state.copy())

		if state == next_state:
			print_board(state)
			break
		elif calculate_objective(state) == calculate_objective(next_state):
			next_state[randint(0, n - 1)] = randint(0, n - 1)
		print_board(state)
		state = next_state
