import random
import matplotlib.pyplot as plt
import numpy as np
import time


"""
After running a bunch of tests, I found out that:
1. it's better to call built-in functions directly without custom functions
2. It's better to create one variable once and use it a lot of times instead of creating the same variable over and over again
"""


# heads = 1 (one step forward) and tails = -1 (one step backwards)
coin_flip = [1, -1]
def calculate(n):
    tosses = [random.choice(coin_flip) for x in range(0, n)]
    ys = [0]
    y_t = 0
    for toss in tosses:
        y_t += toss
        ys.append(y_t)
    return ys


# random walk in 1D and 2D
def walk(n, nrows=1, ncols=1, plots_per_figure=1, in_2D=False, show_computation_time=False):
    start = time.time()
    fig, axes = plt.subplots(nrows, ncols)
    # plt.plot(calculate(n), color="purple")
    # plt.show()
    for row in axes:
        for col in row:
            for i in range(plots_per_figure):
                if in_2D:
                    col.plot(calculate(n), calculate(n))
                else:
                    col.plot(calculate(n))    
    end = time.time()
    if show_computation_time:
        print(f"Elapsed time: {end - start}")
    plt.show()


if __name__=='__main__':
    n = 200000
    walk(n, nrows=2, ncols=3, plots_per_figure=10, in_2D=False, show_computation_time=True)
    

# for i in range(1):
#     test_figures_count = 5
#     start = time.time()

#     for i in range(test_figures_count):
#         plt.plot(calculate(n))
#     plt.axhline(y=0, color="black", linestyle="-")
#     end = time.time()
#     print(f"Elapsed time: {end - start}")
#     plt.grid()
#     plt.show()