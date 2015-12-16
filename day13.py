# -*- coding: utf-8 -*-

import random
import itertools

#BREAKCIRCLE = 0  # part1
BREAKCIRCLE = 1  # part2


def indexOrNeg(arrr, myvalue):
    try:
        return arrr.index(myvalue)
    except:
        return -1    

def readDay13Datafile(myfilename):
    """Reads in the Advent Of Code datafile, which has the list of
       people, potential seating connections, and utilities between them.
       
       Will return:
          n - number of cities
          D - distance matrix
          cities - array (of length n) of city names
    """
    D = {}   # dictionary to hold n times n matrix
    people = []
    
    with open(myfilename) as datafile:
    
        for thisstring in datafile:
            thisstring = thisstring.rstrip()
            thisstring = thisstring[:-1] # remove trailing period
            
            tokens = thisstring.split(' ')
            index_person1 = indexOrNeg(people, tokens[0])
            if index_person1 < 0:
                people.append(tokens[0])
                index_person1 = len(people)-1
            index_person2 = indexOrNeg(people, tokens[10])
            if index_person2 < 0:
                people.append(tokens[10])
                index_person2 = len(people)-1
                
            utils = int(tokens[3])
            if tokens[2] == 'lose':
                utils *= -1
            
            D[index_person1, index_person2] = utils
            # D[index_city2, index_city1] = int(tokens[4])  # NOT SYMMETRIC!
    
    return len(people), D, people
            

def length(tour, D):
    """Calculate the total utility of a seating arrangement via distance matrix 'D'."""
    global BREAKCIRCLE
    if BREAKCIRCLE == 1:
        z = 0
    else:
        z = D[tour[-1], tour[0]]    # edge from last to first city of the tour
        z += D[tour[0], tour[-1]]
    
    for i in range(1,len(tour)):
        z += D[tour[i], tour[i-1]]      # add length of edge from city i-1 to i
        z += D[tour[i-1], tour[i]]      # utility from P1->P2 AND P2<-P1
    return z


def randtour(n):
    """Construct a random tour of size 'n'."""
    sol = list(range(n))      # set solution equal to [0,1,...,n-1]
    random.shuffle(sol) # place it in a random order
    return sol

def printTour(tour, people):
    for iperson in tour:
        print(people[iperson], end=' ')



def all_permutations(n, D, report=None):
    """Do all of the permutations of tours"""
    icount = 0
    bestt = None
    bestz = None
    worstt = None
    worstz = None
    for thistour in itertools.permutations(range(n)):
        icount += 1
        z = length(thistour,D)
        if bestz == None or z < bestz:
            bestz = z
            bestt = list(thistour)
            if report:
                report(z,thistour)
        if worstz == None or z > worstz:
            worstz = z
            worstt = list(thistour)
            if report:
                report(z,thistour)
    
    return bestt, bestz, worstt, worstz


if __name__ == "__main__":
    """Day13:  Travelling Saleman Problem adapted to seating"""
    

    # read in datafile
    n, D, people = readDay13Datafile('day13.dat')
      
        # function for printing best found solution when it is found
    from time import clock
    init = clock()
    def report_sol(obj, s=""):
        print("cpu:%g\tobj:%g\ttour:%s" % \
              (clock(), obj, s))

    print("*** travelling salesman problem for seating***")
    print
            
    # all the permutations
    print("all the permutations!")
    seating_low, z_low, seating_high, z_high = all_permutations(n, D, report_sol)
    assert z_low == length(seating_low,D)

    print("highest utility found solution: z = %g" % z_high)
    printTour(seating_high, people)
    print(" cost={0}".format(z_high))   
   
