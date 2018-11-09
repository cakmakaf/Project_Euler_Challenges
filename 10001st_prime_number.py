# -*- coding: utf-8 -*-
"""
Created on Fri Nov  9 09:16:10 2018

@author: acakmak
"""

#test if p is a prime
def is_p_a_prime(p):
    if p < 2: return
    "Not a prime"
    for i in range(2, int(p**0.5) + 1):
        if p % i == 0:
            return False
    return True

# find the n^th prime
def n_th_Prime(p):
    all_primes = 0
    prime = 1

    while all_primes < p:
        prime += 1
        if is_p_a_prime(prime):
            all_primes += 1
    return prime

print (n_th_Prime(10001))