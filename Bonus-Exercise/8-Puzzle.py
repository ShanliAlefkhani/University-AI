from copy import deepcopy
import time
import itertools

arr = []
for i in range(0,9):
    x = int(input("enter vals :"))
    arr.append(x)
puzzle = [[arr[i + 3 * j] for i in range(3)] for j in range(3)]

goal = [[i + j * 3 for i in range(3)] for j in range(3)]
arr2 = [(0, 1), (0, -1), (1, 0), (-1, 0)]

def print_puzzle(puzzle):
	print("\033[F"*(len(puzzle) + 1))
	print("\n".join(" ".join(str(puzzle[i][j]) for j in range(len(puzzle)))for i in range(len(puzzle))))
	time.sleep(2)

def find_zero(puzzle):
    for i in range(3):
        for j in range(3):
            if puzzle[i][j] == 0:
                return i, j

def best_successor(puzzle, goal):
    b_suc = puzzle
    b = manhattan_distance(puzzle, goal)
    e_x, e_y = find_zero(puzzle)
    for x, y in arr2:
        if e_x + x > 2 or e_x + x < 0 or e_y + y > 2 or e_y + y < 0:
            continue
        suc = deepcopy(puzzle)
        suc[e_x][e_y] = suc[e_x + x][e_y + y]
        suc[e_x + x][e_y + y] = 0
        if manhattan_distance(suc, goal) < b:
            b_suc = suc

    return b_suc

def manhattan_distance(puzzle, goal):
    cout = 0
    for i, j in itertools.product(range(3), range(3)):
        k = puzzle[i][j]
        for ii, jj in itertools.product(range(3), range(3)):
            if goal[ii][jj] == k:
                cout += abs(i - ii) + abs(j - jj)
    return cout


print("\n"*(4), end="")

print_puzzle(puzzle)
while manhattan_distance(puzzle, goal):
    puzzle = best_successor(puzzle, goal)
    print_puzzle(puzzle)
