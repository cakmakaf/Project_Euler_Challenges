# -*- coding: utf-8 -*-
"""
Created on Thu Nov  8 10:56:07 2018

@author: acakmak
"""

def check_palindrome(s):
     """Checks whether the given string is palindrome"""

     if s == s[::-1]:
        return True

product_pal = []
for i in range (999,900,-1):
    for j in range (999,900,-1):
        product = i * j
        if check_palindrome(str(product)):
            product_pal.append(product)
            print("i =" , i , "j = ",j, "for", product)
print (max(product_pal))