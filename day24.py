# -*- coding: utf-8 -*-

import itertools


def evaluateGroup(packages, grouping):
    firstcount = 0
    qe = 1
    weight = [0,0]
    for i in range(len(packages)):
        weight[ grouping[i] ] = weight[ grouping[i] ] + packages[i]
        if (grouping[i] == 0):
            firstcount = firstcount + 1
            qe = qe*packages[i]
    
    equalweights = (3*weight[0]==weight[1])
    return ( equalweights, firstcount, qe)


if __name__ == "__main__":
    """Day24:  Balancing"""

    packages = []
    with open('day24.dat') as datafile:        
        for thisstring in datafile:
            packages.append(int(thisstring))

    # another way of doing this:
    #packages = map(int, [line.strip("\n") for line in open('day24.dat')])
    # from:  https://www.reddit.com/r/adventofcode/comments/3y1s7f/day_24_solutions/

    bestfirstcount = 10000
    bestqe = 100000000000
    bestgroup = None
    
    count = 0
    for group in itertools.product(range(0,2), repeat=len(packages)):
        count = count + 1
        (isequal, firstcount, qe) = evaluateGroup(packages,group)
        if (isequal):
            print("{}.  Equal weights.  firstcount={}, qe={}".format(count,firstcount,qe))
            if (firstcount <= bestfirstcount):
                bestfirstcount=firstcount
                if (qe < bestqe):
                    bestqe = qe
                    bestgroup = group
                    
    
    print("BEST QE={} with {} in first area.  Group={}".format(bestqe, bestfirstcount,bestgroup))
        
