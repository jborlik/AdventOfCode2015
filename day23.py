# -*- coding: utf-8 -*-

import sys

registers = [1, 0]  # registers(0) = a, registers(1) = b
instructions = []

class Instruction:
    def __init__(self, instructionstring):
        self.instruction = ''
        self.register = 0 # or 1
        self.jump = 1 # default move on to next
        self.fullinstruction = instructionstring.rstrip()
        toks = self.fullinstruction.split(' ')
        self.instruction = toks[0]
        
        if (self.instruction == 'hlf'):
            if (toks[1] == 'b'):
                self.register = 1
        elif (self.instruction == 'tpl'):
            if (toks[1] == 'b'):
                self.register = 1
        elif (self.instruction == 'inc'):
            if (toks[1] == 'b'):
                self.register = 1
        elif (self.instruction == 'jmp'):
            self.jump = int(toks[1])
        elif (self.instruction == 'jie'):
            if (toks[1] == 'b,'):
                self.register = 1
            self.jump = int(toks[2])
        elif (self.instruction == 'jio'):
            if (toks[1] == 'b,'):
                self.register = 1
            self.jump = int(toks[2])
        else:
            print ("HUH? parsing {}".format(instructionstring))
            sys.exit()


    
    def executeInstruction(self, registers):
        print(" Executing {}".format(self.instruction), end='')

        myjump = self.jump
        if (self.instruction == 'hlf'):
            registers[self.register] = int(registers[self.register] / 2)

        elif (self.instruction == 'tpl'):
            registers[self.register] = registers[self.register] * 3
            
        elif (self.instruction == 'inc'):
            registers[self.register] = registers[self.register] + 1
            
        elif (self.instruction == 'jmp'):
            pass # already have self.jump
            
        elif (self.instruction == 'jie'):
            if ( registers[self.register] % 2 != 0):
                myjump = 1
            
        elif (self.instruction == 'jio'):
            if ( registers[self.register] != 1):
                myjump = 1
            
        else:
            print ("WHAAAHUH? executing {}".format(self.instruction))
            sys.exit()        
        
        return myjump

if __name__ == "__main__":
    """Day23:  compiler instructions"""
    

    with open('day23.dat') as datafile:
        
        for thisstring in datafile:
            thisIns = Instruction(thisstring)
            instructions.append(thisIns)
            
    # now we have the instructions loaded
    currentinstruction = 0
    count = 0
    while (count < 10000) and (currentinstruction >= 0) and (currentinstruction < len(instructions)) :
        print("Ins {}/{} registers {}".format(currentinstruction,count,registers), end='')
        inc = instructions[currentinstruction].executeInstruction(registers)
        print(" jumping {}".format(inc))
        currentinstruction = currentinstruction + inc
        count = count + 1

    print("Registers: {}".format(registers))    
    
    
    
    