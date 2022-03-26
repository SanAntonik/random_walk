import random
import matplotlib.pyplot as plt
import time


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


# helper function for the function 'walk'
def plot_figure(n, plots_per_figure, in_2D, ax):
    for i in range(plots_per_figure):
        if in_2D:
            ax.plot(calculate(n), calculate(n))
        else:
            ax.plot(calculate(n))


# random walk in 1D and 2D
def walk(n, nrows=1, ncols=1, plots_per_figure=1, in_2D=False, show_computation_time=False):
    start = time.time()
    if nrows == ncols == 1:
        fig, ax = plt.subplots()
        plot_figure(n, plots_per_figure, in_2D, ax)
    elif nrows == 1 and ncols > 1:
        fig, axs = plt.subplots(ncols=ncols)
        for ax in axs:
            plot_figure(n, plots_per_figure, in_2D, ax)
    elif nrows > 1 and ncols == 1:
        fig, axs = plt.subplots(nrows=nrows)
        for ax in axs:
            plot_figure(n, plots_per_figure, in_2D, ax)
    else:
        fig, axs = plt.subplots(nrows, ncols)
        for row in axs:
            for ax in row:
                plot_figure(n, plots_per_figure, in_2D, ax)
    end = time.time()
    if show_computation_time:
        print(f"Elapsed time: {end - start}")
    plt.show()


if __name__ == '__main__':
    n = 25000
    nrows = 3
    ncols = 2
    plots_per_figure = 10
    in_2D = False
    show_computation_time = True
    walk(n, nrows=nrows, ncols=ncols, plots_per_figure=plots_per_figure,
         in_2D=in_2D, show_computation_time=show_computation_time)
