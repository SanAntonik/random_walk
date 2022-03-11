import random
import matplotlib.pyplot as plt
import numpy as np
import time

"""After running a bunch of tests, I found out that:
1. it's better to call built-in functions directly without custom functions
2. It's better to create one variable once and use it a lot of times instead of creating the same variable over and over again
"""

# heads = 1 (one step forward) and tails = -1 (one step backwards)
coin_flip = [1, -1]
n = 100000


def calculate(n):
    tosses = [random.choice(coin_flip) for x in range(0, n)]
    ys = [0]
    y_t = 0
    for toss in tosses:
        y_t += toss
        ys.append(y_t)
    return ys


for i in range(1):
    test_figures_count = 1
    start = time.time()

    for i in range(test_figures_count):
        plt.plot(calculate(n), calculate(n))
    plt.axhline(y=0, color="black", linestyle="-")
    end = time.time()
    print(f"Elapsed time: {end - start}")
    plt.show()

    fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2)
    ax1.plot(calculate(n), calculate(n))
    ax2.plot(calculate(n), calculate(n))
    ax3.plot(calculate(n), calculate(n))
    ax4.plot(calculate(n), calculate(n))

    for ax in fig.get_axes():
        ax.label_outer()
        ax.axhline(y=0, color="black", linestyle="-")
    plt.show()

    # start = time.time()
    # tosses = []
    # ys = []
    # for i in range(test_figures_count):
    #     tosses.append([random.choice(coin_flip) for x in range(0, n)])
    #     ys.append([sum(tosses[i][0:x]) for x in range(0, n)])

    # for y in ys:
    #     plt.plot(y)
    # plt.axhline(y=0, color="black", linestyle="-")
    # end = time.time()
    # print(f"Elapsed time: {end - start}")
    # plt.show()

# tosses = []
# ys = []
# for i in range(0, 4):
#     tosses.append([random.choice(coin_flip) for x in range(0, n)])
#     ys.append([sum(tosses[i][0:x]) for x in range(0, n)])

# fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2)
# ax1.plot(ys[0])
# ax2.plot(ys[1])
# ax3.plot(ys[2])
# ax4.plot(ys[3])

# for ax in fig.get_axes():
#     ax.label_outer()
#     ax.axhline(y=0, color="black", linestyle="-")
# plt.show()


# # # 1D
# def walk_1d(n, subplots_number=1, plots_per_figure=1):
#     pass

# tosses = []
# ys = []
# for i in range(0, 16):
#     tosses.append([random.choice(coin_flip) for x in range(0, n)])
#     ys.append([sum(tosses[i][0:x]) for x in range(0, n)])
#     print(ys, len(ys))
# # print(ys)

# fig, ((ax1, ax2, ax3, ax4), (ax5, ax6, ax7, ax8), (ax9, ax10, ax11, ax12), (ax13, ax14, ax15, ax16)) = plt.subplots(4, 4)
# ax1.plot(ys[0])
# ax2.plot(ys[1])
# ax3.plot(ys[2])
# ax4.plot(ys[3])
# ax5.plot(ys[4])
# ax6.plot(ys[5])
# ax7.plot(ys[6])
# ax8.plot(ys[7])
# ax9.plot(ys[8])
# ax10.plot(ys[9])
# ax11.plot(ys[10])
# ax12.plot(ys[11])
# ax13.plot(ys[12])
# ax14.plot(ys[13])
# ax15.plot(ys[14])
# ax16.plot(ys[15])

# for ax in fig.get_axes():
#     ax.label_outer()
#     ax.axhline(y=0, color="black", linestyle="-")
# plt.show()


# tosses = []
# ys = []
# for i in range(0, 4):
#     tosses.append([random.choice(coin_flip) for x in range(0, n)])
#     ys.append([sum(tosses[i][0:x]) for x in range(0, n)])

# fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2)
# ax1.plot(ys[0])
# ax2.plot(ys[1])
# ax3.plot(ys[2])
# ax4.plot(ys[3])

# for ax in fig.get_axes():
#     ax.label_outer()
#     ax.axhline(y=0, color="black", linestyle="-")
# plt.show()


# tosses = []
# ys = []
# for i in range(0, 4):
#     tosses.append([random.choice(coin_flip) for x in range(0, n)])
#     ys.append([sum(tosses[i][0:x]) for x in range(0, n)])

# for y in ys:
#     plt.plot(y)
# plt.axhline(y=0, color="black", linestyle="-")
# plt.show()


# # 2D
# x_tosses = []
# xs = []
# y_tosses = []
# ys = []
# for i in range(0, 4):
#     x_tosses.append([random.choice(coin_flip) for x in range(0, n)])
#     xs.append([sum(x_tosses[i][0:x]) for x in range(0, n)])
#     y_tosses.append([random.choice(coin_flip) for x in range(0, n)])
#     ys.append([sum(y_tosses[i][0:x]) for x in range(0, n)])

# fig = plt.figure()
# gs = fig.add_gridspec(2, 2, hspace=0, wspace=0)
# (ax1, ax2), (ax3, ax4) = gs.subplots(sharex='col', sharey='row')
# fig.suptitle('Sharing x per column, y per row')
# ax1.plot(xs[0] ,ys[0])
# ax2.plot(xs[1] ,ys[1], 'tab:orange')
# ax3.plot(xs[2] ,ys[2], 'tab:green')
# ax4.plot(xs[3] ,ys[3], 'tab:red')

# for ax in fig.get_axes():
#     ax.label_outer()
#     # ax.axhline(y=0, color="black", linestyle="-")
#     # ax.axvline(x=0, color="black", linestyle="-")
#     ax.grid()
# plt.show()


# x_tosses = []
# xs = []
# y_tosses = []
# ys = []
# for i in range(0, 4):
#     x_tosses.append([random.choice(coin_flip) for x in range(0, n)])
#     xs.append([sum(x_tosses[i][0:x]) for x in range(0, n)])
#     y_tosses.append([random.choice(coin_flip) for x in range(0, n)])
#     ys.append([sum(y_tosses[i][0:x]) for x in range(0, n)])

# fig = plt.figure()
# gs = fig.add_gridspec(2, 2, hspace=0, wspace=0)
# (ax1, ax2), (ax3, ax4) = gs.subplots(sharex='col', sharey='row')
# fig.suptitle('Sharing x per column, y per row')
# ax1.plot(xs[0] ,ys[0])
# ax2.plot(xs[1] ,ys[1], 'tab:orange')
# ax3.plot(xs[2] ,ys[2], 'tab:green')
# ax4.plot(xs[3] ,ys[3], 'tab:red')

# for ax in fig.get_axes():
#     ax.label_outer()
#     # ax.axhline(y=0, color="black", linestyle="-")
#     # ax.axvline(x=0, color="black", linestyle="-")
#     ax.grid()
# plt.show()