#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import division
from __future__ import print_function
import numpy as np

N = 20
T = 1.5
h = 0
L = -1
spins = np.zeros((N,N))

for i in range(N):
    for j in range(N):
        spins[i,j] = 1 if np.random.uniform() < 0.5 else -1

E = 0
for i in range(N):
    for j in range(N):
        x = spins[i, (j-1)%N] + spins[(i-1) % N, j] + spins[i, (j+1)%N] + spins[(i+1)%N, j]
        E = E + L * spins[i,j] * x + h * spins[i,j]

it = 0
while True:
    i = int(np.random.uniform(0,N))
    j = int(np.random.uniform(0,N))
    x = spins[i, (j-1)%N] + spins[(i-1) % N, j] + spins[i, (j+1)%N] + spins[(i+1)%N, j]
    delta = -L * 2 * spins[i,j] * x - 2 * spins[i,j] * h

    if delta < 0 or np.random.uniform() < np.exp(-delta/T):
        spins[i,j] = -spins[i,j]
        E = E + delta

    if it % 100000 == 0:
        print(T, E)
        T = T + 0.01

    it = it + 1
