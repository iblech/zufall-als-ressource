#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import division
from __future__ import print_function

import numpy as np
import matplotlib.pyplot as plt

K = 16     # Anzahl der Kinder
N = K * 7  # Anzahl der Karten
M = 1000   # Anzahl der Durchgänge
D = 7      # Anzahl der Seiten des Würfels
S = 9      # Anzahl erlaubter Startpositionen

frequencies = np.zeros(M)

for i in range(M): #verschiedene Verteilungen der Klassen
    cards = np.random.randint(S, size=N) + 1

    end_positions = np.zeros(N)

    for j in range(K): #die ganze Klasse. wie viele Kindes haben das gleiche ergebnis
        pos = np.random.randint(D)

        while True: #ein Kind
            step = cards[pos]

            if pos + step >= N:
                break

            pos = pos + step

        end_positions[pos] += 1

    frequencies[i] = np.amax(end_positions)/K

plt.hist(frequencies, range=(0,1), bins=100)
plt.show()
