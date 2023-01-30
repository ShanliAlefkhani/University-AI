from firefly import firefly
from matplotlib import pyplot as plt
import time


if __name__ == "__main__":
    for func in [firefly]:
        ns = []
        ts = []
        ls = []
        for n in range(4, 9):
            start = time.time()
            loss = func(n)
            end = time.time()
            ns.append(n)
            ts.append(end - start)
            ls.append(loss)
        plt.plot(ns, ts, label = func.__name__)
        plt.xlabel('n', fontsize=14)
        plt.ylabel('average time', fontsize=14)
        plt.legend()

    plt.savefig(fname = "plot")
