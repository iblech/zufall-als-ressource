#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import division
from __future__ import print_function
import numpy as np
import matplotlib.pyplot as plt

N  = 70
h  = 1/N
dt = 0.00001

V = np.zeros(N)
for i in range(0, int(N/5)):
    V[i] = -10000
for i in range(int(2*N/5), N):
    V[i] = -10000

psi = np.zeros(N, dtype="complex")

for i in range(N):
    V[i] = 1/(i-N/2+0.1) * 500

psi[int(N/3)] = 1

plt.ion()
fig = plt.figure()
ax  = fig.add_subplot(111)
im, = ax.plot(h*np.arange(0,N), np.abs(psi))
fig.canvas.draw()

it = 0
while True:
    Deltapsi = (np.roll(psi, -1) - 2 * psi + np.roll(psi, 1)) / h**2
    Vpsi     = V * psi
    lhs      = -Deltapsi + Vpsi

    psi = psi + dt * lhs/1j
    psi /= np.sqrt(np.sum(np.abs(psi)**2))

#   psi[0]   = 0
#   psi[N-1] = 0

    if it % 500 == 0:
        im.set_ydata(np.abs(psi)**2)
        ax.draw_artist(im)
        im.figure.canvas.blit(im.figure.bbox)
        fig.canvas.draw()

    it += 1

#    if it == 10000:
#        for i in range(int(2*N/5), int(4*N/5)):
#            V[i] = 0
#
#    if it == 50000:
#        for i in range(int(2*N/5), int(3*N/5)):
#            V[i] = -10000
