#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import division
from __future__ import print_function
import numpy as np
import matplotlib.pyplot as plt

N = 20
T = 1.5
h = 0
spins = np.zeros((N,N))

for i in range(N):
    for j in range(N):
        spins[i,j] = 1 if np.random.uniform() < 0.5 else -1

plt.ion()
fig = plt.figure()
ax  = fig.add_subplot(111)
im  = ax.imshow(spins, vmin=0, vmax=1, interpolation="nearest")
fig.canvas.draw()

it = 0
while True:
    i = int(np.random.uniform(0,N))
    j = int(np.random.uniform(0,N))
    x = spins[i, (j-1)%N] + spins[(i-1) % N, j] + spins[i, (j+1)%N] + spins[(i+1)%N, j]
    delta = 2 * spins[i,j] * x - 2 * spins[i,j] * h

    if delta < 0 or np.random.uniform() < np.exp(-delta/T):
        spins[i,j] = -spins[i,j]

    if it % 1000 == 0:
        im.set_data(spins)
        ax.draw_artist(im)
        im.figure.canvas.blit(im.figure.bbox)
        fig.canvas.draw()
        print(it)

    if it > 90000*3:
        pass
    elif it > 90000*2:
        h = h - 1/90000
    elif it > 90000:
        h = h + 1/90000

    it = it + 1

