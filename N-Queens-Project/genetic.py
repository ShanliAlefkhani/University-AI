import itertools
import random
from math import comb
from utils import get_random_state, calculate_objective, print_board


POPULATION_SIZE = 100
MIXING_NUMBER = 2
MUTATION_RATE = 0.05


def fitness_score(state):
    return comb(len(state), 2) - calculate_objective(state)


def random_selection(population, n):
    return [ind for ind in population if random.randrange(comb(n, 2)) < fitness_score(ind)]


def crossover(parents, n):
    cross_points = random.sample(range(n), MIXING_NUMBER - 1)
    offsprings = []
    permutations = list(itertools.permutations(parents, MIXING_NUMBER))
    
    for perm in permutations:
        offspring = []
        start_pt = 0
        
        for parent_idx, cross_point in enumerate(cross_points):
            parent_part = perm[parent_idx][start_pt:cross_point]
            offspring.append(parent_part)
            start_pt = cross_point
            
        last_parent = perm[-1]
        parent_part = last_parent[cross_point:]
        offspring.append(parent_part)
        offsprings.append(list(itertools.chain(*offspring)))
    
    return offsprings


def mutate(state):
    for row in range(len(state)):
        if random.random() < MUTATION_RATE:
            state[row] = random.randrange(len(state))
    return state


def found_goal(states):
    for state in states:
        if calculate_objective(state) == 0:
            return True
    return False


def genetic(n):
    population = [get_random_state(n) for _ in range(POPULATION_SIZE)]
    print("\n"*(n + 1), end="")
        
    while not found_goal(population):
        print_board(sorted(population, key=lambda ind: fitness_score(ind), reverse=True)[0])
        parents = random_selection(population, n)
        offsprings = list(map(mutate, crossover(parents, n)))
        new_gen = offsprings + population
        population =  sorted(new_gen, key=lambda ind: fitness_score(ind), reverse=True)[:POPULATION_SIZE]

    print_board(sorted(population, key=lambda ind: fitness_score(ind), reverse=True)[0])
