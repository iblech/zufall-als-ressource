#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import division
import numpy as np

def normalize(v):
    return v / np.linalg.norm(v)

N  = 200
R  = 0.05
dt = 0.05

x = np.random.rand(3, N)
v = np.random.rand(3, N)
for i in range(N):
    v[:, i] = normalize(v[:, i]) * 4
cummv = np.zeros(N)

it = 0

while True:
    x = x + dt * v

    for i in range(N):
        for j in range(i):
            r   = x[:, i] - x[:, j]
            rsq = np.dot(r,r)

            if rsq > R**2:
                continue

            dv  = np.dot(v[:, i] - v[:, j], r) * r / rsq

            v[:, i], v[:, j] = v[:, i] - dv, v[:, j] + dv

        for k in range(3):
            if x[k,i] < 0 or x[k,i] > 1:
                v[k,i] = -v[k,i]

    cummv = cummv + np.linalg.norm(v, axis=0)**2
    it    = it + 1

    if it % 1 == 0:
        for i in range(N):
#           print("%f\t%f\t%f" % (x[0,i], x[1,i], x[2,i]))
            print("%f" % (cummv[i] / it))
        if it % 1 == 0:
            print("")
