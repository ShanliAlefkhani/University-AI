import time
from collections import Counter
import random


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


def print_board(state):
	print("\033[F"*(len(state) + 1))
	print("\n".join(" ".join("\u2655" if board(i, j, state) else "." for j in range(len(state)))for i in range(len(state))))
	time.sleep(2)


def get_neighbours(state=[]):
    successors = []
    n = len(state)

    for column in range(n):
        for row in range(n):
            if state[column] != row:
                successor = state.copy()
                successor[column] = row
                successors.append(successor)

    return successors


def select_best_neighbours(states, k=1):
	candidates = []

	for state in states:
		state_cost = calculate_objective(state)
		candidates.append([state, state_cost])

	return [item[0] for item in sorted(candidates, key=lambda item: item[1])[:k]]


def get_random_state(n):
	return [random.randint(0, n - 1) for _ in range(n)]


def get_random_neighbours(state, k=1):
        next_states = get_neighbours(state)
        return [random.choice(next_states) for _ in range(k)]
