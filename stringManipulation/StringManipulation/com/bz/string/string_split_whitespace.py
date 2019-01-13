'''
Created on Jan 13, 2019

@author: Boyuan Zhang
'''

#!/bin/python

import re as rr
# Capitalize: string split perserving the whitespace
def solve(s):
    s_array = rr.split(r'(\s+)', s)

    for i in range(0,len(s_array)):
        s_array[i] = s_array[i].capitalize()

    return "".join(s_array)