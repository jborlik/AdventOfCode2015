# -*- coding: utf-8 -*-

class Creature:
    def __init__(self, attack, armor, hp):
        self.attack = attack
        self.armor = armor
        self.hp = hp
        
    def attacks(self, other):
        attackDiff = max(self.attack - other.armor, 1)
        defendDiff = max(other.attack - self.armor, 1)

        roundsToKill = int(other.hp / attackDiff + 0.99)
        roundsToDie = int(self.hp / defendDiff + 0.99)
        print("To kill: {0} rounds, to die: {1} rounds.  {2}".format(roundsToKill, roundsToDie, roundsToDie-roundsToKill))
        return roundsToDie - roundsToKill
        
    def equip(self, sword, armor, ring1, ring2):
        swords = [ (4, 8), (5, 10), (6, 25), (7, 40), (8, 74)]
        armors = [ (0, 0), (1, 13), (2, 31), (3, 53), (4, 75), (5, 102) ]
        rings = [ (0, 0, 0), (1, 0, 25), (2, 0, 50), (3, 0, 100), \
                  (0, 1, 20), (0, 2, 40), (0, 3, 80) ]
                  
        cost = 0
        self.attack = swords[sword][0]
        cost += swords[sword][1]
        self.armor = armors[armor][0]
        cost += armors[armor][1]
        r1_attack, r1_armor, r1_cost = rings[ring1]
        self.attack += r1_attack
        self.armor += r1_armor
        cost += r1_cost
        r2_attack, r2_armor, r2_cost = rings[ring2]
        self.attack += r2_attack
        self.armor += r2_armor
        cost += r2_cost
        
        return cost
        

if __name__ == "__main__":
    """Day21:  RPG"""

    boss = Creature(attack=8, armor=1, hp=104)    
    hero = Creature(attack=7, armor=3, hp=100)
    cost = hero.equip(3,2,0,0)
    
    hero.attacks(boss)
    print("Cost={0}".format(cost))

    print('------------ Least money and win --------------')
    bestcost = 1000000
    for sword in range(0,5):
        for armor in range(0,6):
            for ring1 in range(0,7):
                for ring2 in range(0,7):
                    cost = hero.equip(sword, armor, ring1, ring2)
                    if (cost <= 100):                       
                        rounds = hero.attacks(boss)
                        if (rounds >= 0) and (cost < bestcost):
                            bestcost = cost
                            print("Cost = {0}".format(cost))
                            print('{0}, {1}, {2}, {3}'.format(sword,armor, ring1, ring2))

    print("Best cost = {0}".format(bestcost))
    
    print('------------ Most money and lose --------------')
    worstcost = 0
    for sword in range(0,5):
        for armor in range(0,6):
            for ring1 in range(0,7):
                for ring2 in range(0,7):
                    cost = hero.equip(sword, armor, ring1, ring2)
                    rounds = hero.attacks(boss)
                    if (rounds < 0) and (cost > worstcost):
                        worstcost = cost
                        print("Cost = {0}".format(cost))
                        print('{0}, {1}, {2}, {3}'.format(sword,armor, ring1, ring2))

    print("Worst cost = {0}".format(worstcost))
