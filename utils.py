#!/usr/bin/env python3
import numpy as np

def to_db(value):
        ret = 20*np.log10(value)
        return ret

def print_output(d, PHASE):
        for i in range(len(d)):
                print("% 5f, " % d[i], end='')
                if(i % PHASE == (PHASE-1)):
                        print()