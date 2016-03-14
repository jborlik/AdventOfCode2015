
import copy

# Magic Missile costs 53 mana. It instantly does 4 damage.
# Drain costs 73 mana. It instantly does 2 damage and heals you for 2 hit points.
# Shield costs 113 mana. It starts an effect that lasts for 6 turns. While it is active, your armor is increased by 7.
# Poison costs 173 mana. It starts an effect that lasts for 6 turns. At the start of each turn while it is active, it deals the boss 3 damage.
# Recharge costs 229 mana. It starts an effect that lasts for 5 turns. At the start of each turn while it is active, it gives you 101 new mana.

class Spell:
    def __init__(self, name, cost, effectid, duration, damage, heal, armor, manabonus):
        self.name = name
        self.cost = cost
        self.effectid = effectid
        self.duration = duration
        self.damage = damage
        self.heal = heal
        self.armor = armor
        self.manabonus = manabonus


spells = [ \
    Spell("Magic Missile",  53, 0, 0, 4, 0, 0, 0), \
    Spell("Drain",          73, 0, 0, 2, 2, 0, 0), \
    Spell("Shield",        113, 1, 6, 0, 0, 7, 0), \
    Spell("Poison",        173, 2, 6, 3, 0, 0, 0), \
    Spell("Recharge",      229, 3, 5, 0, 0, 0, 100) ]

bestwin = None

class Gamestate:
    def __init__(self, nextActionID):
        self.hero_hp = 50 # 10 # 50
        self.hero_mana = 500 # 250 # 500
        self.hero_armor = 0
        self.spentmana = 0
        self.boss_hp = 55 # 14 # 55
        self.boss_damage = 8
        self.round = 0
        self.activeeffects = [0,0,0]   # shield, poison, recharge
        self.nextAction = spells[nextActionID]
        self.actionsTaken = [nextActionID]
        self.ishardmode = 1

    def setNextAction(self,nextSpellID):
        self.nextAction = spells[nextSpellID]
        self.actionsTaken.append(nextSpellID)

    def applyEffects(self):
        #   apply effects for player
        self.hero_armor = 0
        for i in range(0,3):
            if (self.activeeffects[i] > 0):
                self.hero_armor = self.hero_armor + spells[i+2].armor
                self.boss_hp = self.boss_hp - spells[i+2].damage
                self.hero_mana = self.hero_mana + spells[i+2].manabonus
                self.activeeffects[i] = self.activeeffects[i] - 1


    def isGameOver(self):
        global bestwin
        if (self.hero_hp <= 0):
            # no, you lost.  Nothing to queue
            #print("Lose, after {} rounds".format(self.round));
            return True
        if (self.boss_hp <= 0):
            # yes, you won!  
            # Check winningqueue if this beats the current best
            #  if it is the best, then replace it
            print("Win!  Mana={}, Rounds={}, Actions={}".format(self.spentmana,self.round,self.actionsTaken))
            if (bestwin == None) or (self.spentmana < bestwin.spentmana):
                bestwin = self
            #  if it is not the best, then just move on
            return True
        return False


    def doTurnAndQueueNext(self,actionqueue):
        global bestwin
        self.round = self.round + 1
        # first apply the current actions
        # player turn:

        if self.ishardmode ==1:
            self.hero_hp = self.hero_hp - 1
            if self.isGameOver():
                return

        self.applyEffects()
        if self.isGameOver():
            return

        # do the action
        if (self.hero_mana < self.nextAction.cost):
            #print("Stopping this chain, as there isn't enough mana to execute the chosen action")
            return
        self.hero_mana = self.hero_mana - self.nextAction.cost
        self.spentmana = self.spentmana + self.nextAction.cost
        if (bestwin != None) and (self.spentmana > bestwin.spentmana):
            # why go on, as this will not be better than the best
            #print("Stopping as bestwin spentmana={} while this activity has spentmana={}".format(bestwin.spentmana, self.spentmana))
            return

        if (self.nextAction.effectid == 0):
            # instantaneous
            self.hero_hp = self.hero_hp + self.nextAction.heal
            self.boss_hp = self.boss_hp - self.nextAction.damage
            if self.isGameOver():
                return
        else:
            # start an effect
            self.activeeffects[self.nextAction.effectid - 1] = self.nextAction.duration
            # i would assert(self.activeffects[effectid-1] == 0)

        self.nextAction = None

        # boss turns:
        self.applyEffects()
        if self.isGameOver():
            return

        self.hero_hp = self.hero_hp - max(self.boss_damage - self.hero_armor, 1)
        if self.isGameOver():
            return

        # what can happen next?
        # I can do instantaneous spells
        gs1 = copy.deepcopy(self)
        gs1.setNextAction(0)
        actionqueue.append(gs1)
        gs2 = copy.deepcopy(self)
        gs2.setNextAction(1)
        actionqueue.append(gs2)
        # I can only do effect spells if they aren't working now
        for i in range(0,3):
            if (self.activeeffects[i] == 0):
                gsi = copy.deepcopy(self)
                gsi.setNextAction(i+2)
                actionqueue.append(gsi)




if __name__ == "__main__":
    """Day22:  Wizard RPG"""

    print("Day 22")

    # Boss:
    # Hit Points: 55
    # Damage: 8

    # Hero:  50 hit points and 500 mana points

    actionqueue = []
    for i in range(0,len(spells)):
        actionqueue.append(Gamestate(i))

    # okay, we are ready to breadth-first search

    itercount = 0
    while (len(actionqueue)>0):
        itercount = itercount + 1
        thisState = actionqueue.pop(0)
        thisState.doTurnAndQueueNext(actionqueue)
        # print("Iter {}: actions = {}".format(itercount,thisState.actionsTaken))
        if (itercount % 100 == 0):
            print("ITERATION {}, queue length {}".format(itercount, len(actionqueue)), end='' )
            if (bestwin==None):
                print(".  No win yet")
            else:
                print(".  Bestwin at {} mana".format(bestwin.spentmana))


    if (bestwin != None):
        print("*** COMPLETE.  Bestwin at {} mana, {} rounds, actions: {}".format(bestwin.spentmana, bestwin.round, bestwin.actionsTaken))
    else:
        print("*** COMPLETE. No winning solutions found!")


        #for part two: 
        # (computed) 1295 is too (high?)
        #  1242 is too low (1295-53)