import time
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


def print_board(state):
	print("\033[F"*(len(state) + 1))
	print("\n".join(" ".join("\u2655" if board(i, j, state) else "." for j in range(len(state)))for i in range(len(state))))
	time.sleep(2)
