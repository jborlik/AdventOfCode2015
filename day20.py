# -*- coding: utf-8 -*-

import functools

def factors(n):    
    return set(functools.reduce(list.__add__, 
                ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))
       
def sumCloseFactors(myfactors, maxuseoffactor, basenumber, multiplier):
    retval = 0
    for i in myfactors:
        if basenumber < i*maxuseoffactor:
            retval += i*multiplier
    return retval
                

if __name__ == "__main__":
    """Day20:  Factorization"""
    
    target = 36000000

    for i in range(800000,1000000):
        myfactors = factors(i)
        sumoffactors = sum(myfactors)
        print("{0}: {1}".format(i,sumoffactors*10))
        if sumoffactors*10 >= target:
            break

    print("First house with presents > 36000000 is {0}".format(i))
    
    for i in range(10000,1000000):
        presentsathouse = sumCloseFactors(factors(i), 50, i, 11)
        print("House {0}:  {1} presents".format(i,presentsathouse))
        if (presentsathouse >= target):
            break

    print("First house with presents > 36000000 for lazy elves is {0}".format(i))

    