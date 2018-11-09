# -*- coding: utf-8 -*-
"""
Created on Fri Nov  9 09:00:09 2018

@author: acakmak
"""

n = range(0, 101)
x = sum(n)
print (x * x - sum(i*i for i in n))