#!/usr/bin/python3

from Crypto.Random import random
from random import randint
from math import log2,ceil
from time import time
from fractions import gcd

def modifiedPower(a,b,mod):
    return pow(a,b,mod)

def euclid(n,m):
    if(m==0):
        return n,1,0
    else:
        g,a,b = euclid(m,n%m)
        return g,b,(a-((n/m)*b))

def euclidInbuilt(n,m):
    return gcd(n,m)

def millerRabinPrimalityTest(prime):
    bits = ceil(log2(prime))
    for _ in range(0,20):
        n=randint(3,1<<bits)
        while(euclidInbuilt(n,prime)!=1):
            n=randint(3,1<<bits)
        if(modifiedPower(n,prime-1,prime)!=1):
            return False
    return True

def generatePrime(security):
    while True:
        prime = randint(3,1<<security)
        if(millerRabinPrimalityTest(prime)):
            break
    return prime

# if __name__ == '__main__':
#     start = time()
#     print (generatePrime(1024))
#     end=time()
#     print (end-start)
