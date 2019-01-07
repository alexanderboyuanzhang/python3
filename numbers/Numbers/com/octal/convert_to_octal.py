'''
Created on Jan 7, 2019

@author: Boyuan Zhang 2
'''


def convert_to_octal(n):
    res = str(oct(n))[2:]
    return res


# decimal number
dec = 14

o = str(convert_to_octal(dec))
print(o)
print(len(o))