# -*- coding: utf-8 -*-
"""
Created on Thu Nov  8 10:32:48 2018

@author: acakmak
"""
def max_factor(n):

    factor = 2
    while factor * factor <= n:
        while n % factor == 0:
            n /= factor
        factor += 1
    if (n > 1):
        return n
    return factor

print (max_factor(600851475143))