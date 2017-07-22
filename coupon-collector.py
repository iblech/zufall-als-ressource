#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import division
from __future__ import print_function
import numpy as np
import sys

def drawGeometric(p):
    return np.ceil(np.log(1 - np.random.uniform()) / np.log(1 - p))

N = 680

while True:
    x = 1
    for k in range(1,N):
        x = x + drawGeometric((N - k) / N)
    print(x)
    sys.stdout.flush()
