#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import division
from __future__ import print_function
import numpy as np
import sys

def drawGeometric(p):
    return np.ceil(np.log(1 - np.random.uniform()) / np.log(1 - p))

N = 680

x = np.zeros(N)
for k in range(1,N):
    x[k-1] = drawGeometric((N - k) / N)

it = 0
while True:
    k = int(np.random.uniform(N-1)) + 1
    x[k-1] = drawGeometric((N - k) / N)
    if it % 100 == 0:
        print(np.sum(x))
        sys.stdout.flush()
    it = it + 1
