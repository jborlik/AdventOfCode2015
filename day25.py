# -*- coding: utf-8 -*-

def codegen():
    """Generator for the next code based for Day 25"""
    codeNum = 20151125 # code for day 1,1
    while True:
        yield codeNum
        multmp = codeNum*252533
        codeNum = multmp % 33554393   # for next iteration

if __name__ == "__main__":
    """Day25:  generating code"""

    # To continue, please consult the code grid in the manual.  
    # Enter the code at row 2981, column 3075.

    count = 1
    row = 1
    column = 1
    
    codes = codegen()
    
    maxcount = 2981*3075*100
    while (count < maxcount):
        code = next(codes)
        if (count % 1000 == 0):
            print("({},{})={}".format(row,column,code))
        if (row==2981)and(column==3075):
            print("({},{})={}".format(row,column,code))
            break
        count = count + 1
        if (row == 1):
            row = column + 1
            column = 1
        else:
            row = row -1
            column = column + 1
    
    print("DONE with {}".format(count))
    