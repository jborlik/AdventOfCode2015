# -*- coding: utf-8 -*-

#  Today, the Elves are playing a game called look-and-say. 
#  They take turns making sequences by reading aloud the previous sequence 
#  and using that reading as the next sequence. For example, 211 is read 
#  as "one two, two ones", which becomes 1221 (1 2, 2 1s).

# For example:
#
# 1 becomes 11 (1 copy of digit 1).
# 11 becomes 21 (2 copies of digit 1).
# 21 becomes 1211 (one 2 followed by one 1).
# 1211 becomes 111221 (one 1, one 2, and two 1s).
# 111221 becomes 312211 (three 1s, two 2s, and one 1).

# puzzleinput = '3113322113'


def lookAndSay(thisseq):
    retval = ''
    lastchar = ''
    numchar = 0    
    for achar in thisseq:
        if achar != lastchar:
            # output and reset counter
            if lastchar:
                retval += '{0}{1}'.format(numchar,lastchar)
            numchar = 1
            lastchar = achar
        else:
            numchar += 1

    # output the rest at the end
    retval +=  '{0}{1}'.format(numchar,lastchar)
    return retval



if __name__ == "__main__":
    """Advent of Code Day 10"""

    puzzleinput = '3113322113'
    for i in range(40):
        puzzleinput = lookAndSay(puzzleinput)
        #print(puzzleinput)
    
    print("length of result for 40 iter: {0}".format(len(puzzleinput)))
    len_from_40 = len(puzzleinput)
    
    puzzleinput = '3113322113'
    for i in range(50):
        puzzleinput = lookAndSay(puzzleinput)
        #print(puzzleinput)
    
    print("length of result for 50 iter: {0}".format(len(puzzleinput)))
    len_from_50 = len(puzzleinput)
    
    conway = 1.303577269

    print('conway predicts 50 as: {0}'.format(len_from_40*conway**10))
    