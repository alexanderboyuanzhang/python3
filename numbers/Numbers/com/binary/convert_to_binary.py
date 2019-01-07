'''
Created on Jan 7, 2019

@author: Boyuan Zhang
'''


def convertToBinary(n):
    res = ""
    while(n>=1):
        res = str(n%2) + res 
        print(res)
        n=n//2
    return res


# decimal number
dec = 17

o = str(convertToBinary(dec))
print(o)
print(len(o))

