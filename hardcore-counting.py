#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import division
from __future__ import print_function
import numpy as np
import matplotlib.pyplot as plt

def make_sampler(n,m):
    x = np.zeros((n,m))

    def draw():
        i = np.random.randint(n)
        j = np.random.randint(m)

        if x[i,j] == 1:
            x[i,j] = 0
        elif (i == 0 or x[i-1,j] == 0) and (i == n-1 or x[i+1,j] == 0) and (j == 0 or x[i,j-1] == 0) and (j == m-1 or x[i,j+1] == 0):
            x[i,j] = 1

        return x

    for i in range(1000):
        draw()

    return draw

N = 10000

def proportion(sampler, f):
    global N
    c = 0
    for i in range(N):
        if f(sampler()):
            c += 1
    return c / N

def has_zero_first_row(A):
    return np.count_nonzero(A[0,:]) == 0

# für 4x4
a = proportion(make_sampler(4,4), has_zero_first_row)
b = proportion(make_sampler(3,4), has_zero_first_row)
c = proportion(make_sampler(2,4), has_zero_first_row)
d = proportion(make_sampler(1,4), has_zero_first_row)
print(a,b,c,d)
print(1/(a*b*c*d))

# für 3x3
b = proportion(make_sampler(3,3), has_zero_first_row)
c = proportion(make_sampler(2,3), has_zero_first_row)
d = proportion(make_sampler(1,3), has_zero_first_row)
print(b,c,d)
print(1/(b*c*d))

# für 2x2
c = proportion(make_sampler(2,2), has_zero_first_row)
d = proportion(make_sampler(1,2), has_zero_first_row)
print(c,d)
print(1/(c*d))

# für DxD, mehrere Durchgänge
D = 10

for i in range(10):
    for i in range(10):
        p = 1
        for i in range(1,D+1):
            q = proportion(make_sampler(i,D), has_zero_first_row)
            p /= q
        print(N,p)
    N *= 2
