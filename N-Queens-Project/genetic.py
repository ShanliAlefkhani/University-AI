import itertools
import random
from math import comb
from utils import get_random_state, calculate_objective

NUM_QUEENS = 8
POPULATION_SIZE = 10
MIXING_NUMBER = 2
MUTATION_RATE = 0.05


def fitness_score(seq):
    return 28 - calculate_objective(seq)


def selection(population):
    return [ind for ind in population if random.randrange(comb(NUM_QUEENS, 2)*2) < fitness_score(ind)]


def crossover(parents):
    cross_points = random.sample(range(NUM_QUEENS), MIXING_NUMBER - 1)
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


def mutate(seq):
    for row in range(len(seq)):
        if random.random() < MUTATION_RATE:
            seq[row] = random.randrange(NUM_QUEENS)
    return seq


def print_found_goal(population):
    for ind in population:
        score = fitness_score(ind)
        print(f'{ind}. Score: {score}')
        if score == comb(NUM_QUEENS, 2):
            return True
    return False


population = [get_random_state(NUM_QUEENS) for _ in range(POPULATION_SIZE)]
    
while not print_found_goal(population):
    parents = selection(population)
    offsprings = list(map(mutate, crossover(parents)))
    new_gen = offsprings + population
    population =  sorted(new_gen, key=lambda ind: fitness_score(ind), reverse=True)[:POPULATION_SIZE]
