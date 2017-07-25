#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import division
from __future__ import print_function
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

def draw(p):
    u = np.random.uniform()
    v = 0
    for i in range(len(p)):
        if v + p[i] >= u:
            return i
        v = v + p[i]
    return len(p) - 1

T = np.array([[0.5, 0.25, 0.25], [0.5, 0, 0.5], [0.25, 0.25, 0.5]])

N = 30
K = 50000

hits = np.zeros((N, 3))

for i in range(K):
    x = 0
    for j in range(N):
        x = draw(T[x,:])
        hits[j,x] = hits[j,x] + 1

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
nbins = 3

for z in range(N):
    ax.bar([0,1,2], hits[z,:]/K, zs=z, zdir='y', alpha=0.8, width=0.1)

plt.show()
