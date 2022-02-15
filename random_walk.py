import random
import collections
import matplotlib.pyplot as plt
import numpy as np

print("Hello")
a = 55
b = 7
print(f"{a} mod {b} = {a % b}")


# heads = 1 (one step forward) and tails = -1 (one step backwards)
coin_flip = ["heads", "tails"]

for i in range(0, 10):
    tosses = [random.choice(coin_flip) for x in range(0, 100)]
    # print(random.choice(coin_flip))
    print(collections.Counter(tosses))

# print(plt.__version__)
# print(np.random.seed(444))

plt.plot([1, 2, 3, 4], [18, 2, 3, 4], 'ro')

t = np.arange(0., 5., 0.2)
plt.plot(t, t, 'r--', t, t**2, 'bs', t, t**3, 'g^')

plt.ylabel("some numbers")
plt.show()
