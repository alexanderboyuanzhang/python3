'''
Created on Jan 7, 2019

@author: Boyuan Zhang 2
'''


def convert_to_hexadecimal(n):
    res = str(hex(n))[2:].upper()
    return res

# decimal number
dec = 14

o = str(convert_to_hexadecimal(dec))
print(o)
print(len(o))