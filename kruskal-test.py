#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import division
from __future__ import print_function

import numpy as np

K = 16     # Anzahl der Kinder
N = K * 7  # Anzahl der Karten
M = 2000   # Anzahl der Durchgänge
D = 7      # Anzahl der Seiten des Würfels
S = 9      # Anzahl erlaubter Startpositionen

sum_of_frequency = 0

for i in range(M): #verschiedene Verteilungen der Klassen
    cards = np.random.randint(S, size=N) + 1

    end_positions = np.zeros(N)

    for i in range(K): #die ganze Klasse. wie viele Kindes haben das gleiche ergebnis
        pos = np.random.randint(D)

        while True: #ein Kind
            step = cards[pos]

            if pos + step >= N:
                break

            pos = pos + step

        end_positions[pos] += 1

    single_frequency = np.amax(end_positions)/K

    sum_of_frequency += single_frequency
    print(single_frequency)

#print("Die durchschnittliche Frequenz: %f" %(sum_of_frequency/M))
