from scipy import stats
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


samples = []

start = 0

for i in range(50000):
    turn = -0.05
    if np.random.binomial(1, 0.5):
        turn = 0.05
    turn_likelihood = stats.norm.pdf(start + turn) * stats.norm.pdf(start)
    current_likelihood = stats.norm.pdf(start) * stats.norm.pdf(start)
    if turn_likelihood >= current_likelihood:
        start = start + turn
        samples.append(start)
        continue
    else:
        if np.random.binomial(1, (turn_likelihood / current_likelihood)):
            start = start + turn
            samples.append(start)
            continue
        else:
            continue

samples = samples[2500:]




plt.figure(dpi=300)

plt.hist(samples, 100, normed=1)

plt.show()


print np.mean(samples)
print np.std(samples)
