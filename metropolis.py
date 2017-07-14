#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Aufruf mit:
# ./% | ~/sgnuplot.sh "" "w lp, sqrt(2/pi)*x**2*exp(-x**2/2)/10" | gnuplot - 2>/dev/null

from __future__ import division
from __future__ import print_function
import numpy as np
import sys

def f(x):
    a = 1
    if x < 0:
        return 0
    else:
        return np.sqrt(2/np.pi) * x**2 * np.exp(-x**2 / (2*a**2)) / a**3

def g(x):
    return np.random.normal(x, 0.1)

N    = 50
hist = np.zeros(N)

x = 0
it = 0

while True:
    y = g(x)
    u = np.random.uniform()
    if u < f(y)/f(x):
        x = y

    z = np.floor(x/0.1)
    if z < N:
        hist[z] = hist[z] + 1
    it = it + 1

    if it % 100 == 0:
        print(it, file=sys.stderr)

        for i in range(N):
            print("%f\t%f" % (i*0.1, hist[i] / it))
        print("")
