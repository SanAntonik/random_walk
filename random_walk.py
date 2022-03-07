import random
import collections
import matplotlib.pyplot as plt
import numpy as np


# heads = 1 (one step forward) and tails = -1 (one step backwards)
coin_flip = [1, -1]
n = 1000


# tosses = []
# ys = []
# for i in range(0, 16):
#     tosses.append([random.choice(coin_flip) for x in range(0, n)])
#     ys.append([sum(tosses[i][0:x]) for x in range(0, n)])
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


x_tosses = []
xs = []
y_tosses = []
ys = []
for i in range(0, 4):
    x_tosses.append([random.choice(coin_flip) for x in range(0, n)])
    xs.append([sum(x_tosses[i][0:x]) for x in range(0, n)])
    y_tosses.append([random.choice(coin_flip) for x in range(0, n)])
    ys.append([sum(y_tosses[i][0:x]) for x in range(0, n)])

fig = plt.figure()
gs = fig.add_gridspec(2, 2, hspace=0, wspace=0)
(ax1, ax2), (ax3, ax4) = gs.subplots(sharex='col', sharey='row')
fig.suptitle('Sharing x per column, y per row')
ax1.plot(xs[0] ,ys[0])
ax2.plot(xs[1] ,ys[1], 'tab:orange')
ax3.plot(xs[2] ,ys[2], 'tab:green')
ax4.plot(xs[3] ,ys[3], 'tab:red')

for ax in fig.get_axes():
    ax.label_outer()
    # ax.axhline(y=0, color="black", linestyle="-")
    # ax.axvline(x=0, color="black", linestyle="-")
    ax.grid()
plt.show()
    # plt.plot(tosses)
    # print(tosses)
    # # print(random.choice(coin_flip))
    # print(collections.Counter(tosses))




# print(plt.__version__)
# print(np.random.seed(444))

# plt.plot([1, 2, 3, 4], [18, 2, 3, 4], 'ro')

# t = np.arange(0., 5., 0.2)
# plt.plot(t, t, 'r--', t, t**2, 'bs', t, t**3, 'g^')

# plt.ylabel("some numbers")
# plt.show()
