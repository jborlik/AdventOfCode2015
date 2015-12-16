# -*- coding: utf-8 -*-


import numpy as np
from scipy.optimize import minimize

#Sprinkles: capacity 2, durability 0, flavor -2, texture 0, calories 3
#Butterscotch: capacity 0, durability 5, flavor -3, texture 0, calories 3
#Chocolate: capacity 0, durability 0, flavor 5, texture -1, calories 8
#Candy: capacity 0, durability -1, flavor 0, texture 5, calories 8


    

def score(receipe, ingredients):
    weighted = np.dot(receipe, ingredients)
    totcalories = weighted[0,-1]
    weighted = np.delete(weighted, 4, 1)
    weighted = np.clip(weighted, 0, 100000)
    retval = np.cumprod(weighted,1)
    return retval[0,-1], totcalories

  
    
if __name__ == "__main__":
    """Day15: Optimization"""

    test_ingr = np.matrix([ [-1, -2, 6, 3, 8], \
                             [2,  3,-2,-1, 3] ], dtype=int)  

                             
    test_receipe = np.matrix([44, 56])
    test_score, calories = score(test_receipe, test_ingr)
    assert test_score == 62842880  # as per writeup
    
    
    ingredients = np.matrix([ [2, 0, -2, 0, 3], \
              [0, 5, -3, 0, 3], \
              [0, 0,  5,-1, 8], \
             [0,-1,  0, 5, 8] ], dtype=int)    
    
    score_highest = 0
    receipe_highest = None
    
    for ing1 in range(0,100):
        for ing2 in range(0,100):
            for ing3 in range(0,100):
                sum = ing1+ing2+ing3
                if sum > 100:
                    continue
                receipe = np.matrix([ ing1, ing2, ing3, 100-sum ]) 
                thisscore, calories = score(receipe, ingredients)
                print("Score {0} calories {1} -> {1}".format(thisscore, calories, receipe))
                if (calories != 500):
                    continue
                if thisscore > score_highest:
                    score_highest = thisscore
                    receipe_highest = receipe
                
    
    print("Best score: {0} with receipe {1}".format(score_highest, receipe_highest))
    

    
                             
    