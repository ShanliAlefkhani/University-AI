from hill_climbing import hill_climbing
from simulated_annealing import simulated_annealing
from local_beam_search import local_beam_search
from genetic import genetic
from matplotlib import pyplot as plt
import time


if __name__ == "__main__":
    for func in [hill_climbing, simulated_annealing, local_beam_search, genetic]:
        ns = []
        ts = []
        for n in range(4, 9):
            start = time.time()
            func(n)
            end = time.time()
            ns.append(n)
            ts.append(end - start)
        plt.plot(ns, ts, label = func.__name__)
        plt.xlabel('n', fontsize=14)
        plt.ylabel('running time', fontsize=14)
        plt.legend()

    plt.savefig(fname = "plot")
