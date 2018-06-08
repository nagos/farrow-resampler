#!/usr/bin/env python3
import numpy as np

def blackman(M, p, sym=True):
        # Docstring adapted from NumPy's blackman function
        if M < 1:
                return np.array([])
        if M == 1:
                return np.ones(1, 'd')
        odd = M % 2
        if not sym and not odd:
                M = M + 1
        n = np.arange(0, M)+p
        w = (0.42 - 0.5 * np.cos(2.0 * np.pi * n / (M - 1)) +
                0.08 * np.cos(4.0 * np.pi * n / (M - 1)))
        if(p):
                w[-1] = w[-2]/200
        return w

def get_c(N, p, F = 0.5):
        if(F>1):
                F = 1
        alpha = 0.5 * (N - 1)
        m = np.arange(0, N) - alpha + p
        h = F * np.sinc(F * m)

        win = blackman(N, p)
        h *= win

        s = np.sum(h)
        h /= s
        return h

def to_db(value):
        ret = 20*np.log10(value)
        return ret

def print_output(d, PHASE):
        for i in range(len(d)):
                print("% .10e, " % d[i], end='')
                if(i % PHASE == (PHASE-1)):
                        print()
