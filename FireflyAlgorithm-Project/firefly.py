import itertools
import numpy as np
from numpy.random import default_rng


POP_SIZE = 1000
MAX_EVALS = 1010
ALPHA = 1.0
BETA = 10.0
GAMMA = 0.01


def loss_function(x):
    objective = 0
    for i, j in itertools.product(range(x.shape[0]), range(x.shape[1])):
        for p, q in itertools.product(range(x.shape[0]), range(x.shape[1])):
            if i == p and j == q:
                continue
            if i == p or j == q or abs(i - p) == abs(j - q): 
                objective += x[i, j] * x[p, q]
    return objective - (3.0 * np.sum(x))


def firefly(n):
    lb=0
    ub=1
    fireflies = default_rng(None).uniform(lb, ub, (POP_SIZE, n, n))
    intensity = [loss_function(fireflies[i]) for i in range(POP_SIZE)]
    best = np.min(intensity)

    evaluations = POP_SIZE
    new_alpha = ALPHA
    search_range = ub - lb
    f = fireflies[np.argmin(intensity)]

    while evaluations <= MAX_EVALS:
        new_alpha *= 0.99
        for i in range(POP_SIZE):
            for j in range(POP_SIZE):
                if intensity[i] > intensity[j]:
                    r = np.sum(np.square(fireflies[i] - fireflies[j]))
                    beta = BETA * np.exp(-GAMMA * r)
                    steps = new_alpha * (default_rng(None).random(n) - 0.5) * search_range
                    fireflies[i] += beta * (fireflies[j] - fireflies[i]) + steps
                    fireflies[i] = np.clip(fireflies[i], lb, ub)
                    intensity[i] = loss_function(fireflies[i])
                    evaluations += 1
                    if intensity[i] < best:
                        best = intensity[i]
                        f = fireflies[i].copy()
    print(f)
    print()
    print(best)
    return best
