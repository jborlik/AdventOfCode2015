# -*- coding: utf-8 -*-

# Reindeer can only either be flying (always at their top speed) or 
# resting (not moving at all), and always spend whole seconds in either state.

class Reindeer:
    def __init__(self, instructionstring):
        if (len(instructionstring) == 0):
            self.name = ''
            self.flyspeed = 0
            self.flytime = 0
            self.resttime = 0
        else:
            toks = instructionstring.split(' ')
            self.name = toks[0]
            self.flyspeed = int(toks[3])
            self.flytime = int(toks[6])
            self.resttime = int(toks[13])
        self.distance = 0
        self.isflying= True
        self.timeInState = 0
        self.points = 0
    
    def reset(self):
        self.distance = 0
        self.isflying= True
        self.timeInState = 0
        self.points = 0
    
    def incrementOneSec(self):
        self.timeInState += 1
        if self.isflying == True:
            self.distance += self.flyspeed
            if (self.timeInState == self.flytime):
                self.isflying = False
                self.timeInState = 0
        else:
            self.distance += 0
            if (self.timeInState == self.resttime):
                self.isflying = True
                self.timeInState = 0

if __name__ == "__main__":
    """Day14:  Reindeer flight simulation"""

    r1 = Reindeer('')
    r1.name = 'Comet'
    r1.flyspeed = 14
    r1.flytime = 10
    r1.resttime = 127
    
    for time in range(1,1001):
        r1.incrementOneSec()
        print("Time {0}: Deer {1} at {2} km, flying={3}".format(time, r1.name, r1.distance, r1.isflying))


    print("********* Reindeer ********")
    deers = {}
    with open('day14.dat') as datafile:
        for thisstring in datafile:
            thisDeer = Reindeer( thisstring.rstrip() )
            deers[thisDeer.name] = thisDeer

#    r1.reset()
#    deers = {}
#    deers[r1.name] = r1
#    r2 = Reindeer('')
#    r2.name = 'Dancer'
#    r2.flyspeed = 16
#    r2.flytime = 11
#    r2.resttime = 162
#    deers[r2.name] = r2

    
    maxDist = 0
    maxDeer = None

    #for time in range(1,1000+1):
    for time in range(1,2503+1):
        maxDist = 0
        maxDeer = None    
        for (name,thisDeer) in deers.items():
            thisDeer.incrementOneSec()
            if thisDeer.distance == maxDist:
                thisDeer.points += 1
            elif (thisDeer.distance > maxDist):
                maxDist = thisDeer.distance
                maxDeer = thisDeer
                
        # award a point to the winning deer for this slice
        maxDeer.points += 1
        print("Time {0}: Winning deer {1} ({2} points)".format(time, maxDeer.name, maxDeer.points))
    
    
    print("Winning deer {0} at {1} km".format(maxDeer.name,maxDist))
            
    mostPoints = 0
    mostPointedDeer = None
    for (name,thisDeer) in deers.items():
        if (thisDeer.points > mostPoints):
            mostPoints = thisDeer.points
            mostPointedDeer = thisDeer        
    
    print("Deer with most points {0} at {1} pts".format(mostPointedDeer.name,mostPoints))
        