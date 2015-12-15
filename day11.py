# -*- coding: utf-8 -*-

#--- Day 11: Corporate Policy ---
#
#Santa's previous password expired, and he needs help choosing a new one.
#
#To help him remember his new password after the old one expires, Santa has
# devised a method of coming up with a password based on the previous one. 
# Corporate policy dictates that passwords must be exactly eight lowercase letters 
# (for security reasons), so he finds his new password by incrementing his old
# password string repeatedly until it is valid.
#
#Incrementing is just like counting with numbers: xx, xy, xz, ya, yb, and so on. 
#Increase the rightmost letter one step; if it was z, it wraps around to a, and 
#repeat with the next letter to the left until one doesn't wrap around.
#
#Unfortunately for Santa, a new Security-Elf recently started, and he has imposed
# some additional password requirements:
#
#Passwords must include one increasing straight of at least three letters, like
# abc, bcd, cde, and so on, up to xyz. They cannot skip letters; abd doesn't count.
# 
#Passwords may not contain the letters i, o, or l, as these letters can be mistaken
# for other characters and are therefore confusing.:
#     
#Passwords must contain at least two different, non-overlapping pairs of letters, like aa, bb, or zz.
#For example:
#
#hijklmmn meets the first requirement (because it contains the straight hij) but
# fails the second requirement requirement (because it contains i and l).
#abbceffg meets the third requirement (because it repeats bb and ff) but fails 
# the first requirement.
#abbcegjk fails the third requirement, because it only has one double letter (bb).
#The next password after abcdefgh is abcdffaa.
#The next password after ghijklmn is ghjaabcc, because you eventually skip all the
# passwords that start with ghi..., since i is not allowed.
#Given Santa's current password (your puzzle input), what should his next password be?

import re



#  http://ubuntuforums.org/showthread.php?t=1584242


class IncString(str):
    def __add__(self, x):
        # If we're trying to add anything but an int, do normal string
        # addition.
        if type(x) is not int:
            return str.__add__(self, x)

        res = ''
        i = len(self)-1
        while x > 0:
            # Get the ASCII code of the i-th letter and "normalize" it
            # so that a is 0, b is 1, etc.
            # If we are at the end of the string, make it -1, so that if we
            # need to "add" 1, we get a.
            if i >= 0:
                c = ord(self[i]) - 97
            else:
                c = -1

            # Calculate the number of positions by which the letter is to be
            # "rotated".
            pos = x % 26

            # Calculate x for the next letter, add a "carry" if needed.
            x //= 26
            if c + pos >= 26:
                x += 1

            # Do the "rotation".
            c = (c + pos) % 26

            # Add the letter at the beginning of the string.
            res = chr(c + 97) + res

            i -= 1

        # If we didn't reach the end of the string, add the rest of the string back.
        if i >= 0:
            res = self[:i+1] + res

        return IncString(res)
        



if __name__ == "__main__":
    """Day 11, string manipulation"""
    
    passwd = IncString('cqjxxyzz')   #day2
    #passwd = IncString('cqjxjnds')  #day1... result cqjxxyzz
    #passwd = IncString('abcdefgh')  #test... result abcdffaa

    test1list = ('abc', 'bcd','cde','def','efg','fgh','pqr','rst','stu','tuv','uvw','vwx','wxy','xyz')
    re_test2 = re.compile(r'[iol]')  # fails if it contains i, o, l
    re_test3 = re.compile(r'(\w)\1\w*(\w)\2') # succeeds if duplicate letters
    
    while True:
        passwd += 1
        print('Testing {0}: '.format(passwd),end='')
        
        if any(s in passwd for s in test1list):
            # we found a match for test1
            print('ok ', end='')
            
            if re_test2.search(passwd) == None:
                # we didn't find am i, o, l
                print('ok ', end='')
                
                if re_test3.search(passwd) != None:
                    # we found a duplicate
                    print('ok')
                    break
                else:
                    print('FAIL_duplicate')
            else:
                print('FAIL_iol')
        else:
            print('FAIL_triple')
    
    print('Next password: {0}'.format(passwd))
    
                    
        
    
    
    
    
    

