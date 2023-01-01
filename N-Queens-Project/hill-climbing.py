from random import randint
from collections import Counter


def board(i, j, state):
	return int(state[j] == i)


def calculate_objective(state):
	x = 0
	for v in Counter(state).values():
		x += v * (v - 1) / 2

	for i in range(len(state)):
		for j in range(i + 1, len(state)):
			if abs(i - j) == abs(state[i] - state[j]):
				x += 1
	return int(x)


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

	while True:
		next_state = get_neighbour(state.copy())

		if state == next_state:
			print("\n".join(" ".join(str(board(i, j, state)) for j in range(n))for i in range(n)))
			break
		elif calculate_objective(state) == calculate_objective(next_state):
			next_state[randint(0, n - 1)] = randint(0, n - 1)

		state = next_state
