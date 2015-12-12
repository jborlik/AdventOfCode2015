# -*- coding: utf-8 -*-
import re

 # test1:  containts three vowels
re_test1 = re.compile(r'[^aeiou]*[aeiou][^aeiou]*[aeiou][^aeiou]*[aeiou]\w*')

# test2:  one letter appears twice in a row
re_test2 = re.compile(r'(\w)\1')

# test3:  does NOT contain "ab", "cd", "pq", "xy"
re_test3_1 = re.compile(r'ab')
re_test3_2 = re.compile(r'cd')
re_test3_3 = re.compile(r'pq')
re_test3_4 = re.compile(r'xy')

# day2 test1:  It contains a pair of any two letters that appears at least twice (nonoverlapping)
re_test4 = re.compile(r'(\w\w)\w*\1')

# day2 test2:  one letter which repeats with exactly one letter between them, like xyx
re_test5 = re.compile(r'(\w)\w\1')


goodwords = 0
badwords = 0
icount = 0

iday = 2


with open('day5.dat') as datafile:
    
    for thisword in datafile:
        thisword = thisword.rstrip()
        icount += 1

        print('{0}: {1} '.format(icount,thisword), end='')
        
        if iday==1:
            
            # test1:  containts three vowels
            if (re_test1.match(thisword)):
                print("OK ", end='')
            else:
                print("BAD")
                badwords += 1
                continue
            
            # test2:  one letter appears twice in a row
            m = re_test2.search(thisword)
            if m:
                print("OK ", end='')
            else:
                print("BAD")
                badwords += 1
                continue
            
            # test3: does not contain "ab", "cd", "pq", "xy"
            if (re_test3_1.search(thisword) or \
                re_test3_2.search(thisword) or \
                re_test3_3.search(thisword) or \
                re_test3_4.search(thisword) ):
    
                print("BAD")
                badwords +=1
                continue
            else:
                print("OK")
                
        if iday==2:
            # day2 test1:  It contains a pair of any two letters that appears at least twice (nonoverlapping)
            m = re_test4.search(thisword)
            if m:
                print("OK ", end='')
            else:
                print("BAD")
                badwords += 1
                continue
            
            # day2 test2:  one letter which repeats with exactly one letter between them, like xyx
            m = re_test5.search(thisword)
            if m:
                print("OK ", end='')
            else:
                print("BAD")
                badwords += 1
                continue            

        goodwords += 1

print("{0} total words, {1} good and {2} bad".format(icount,goodwords,badwords))

        
        
        