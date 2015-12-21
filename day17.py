# -*- coding: utf-8 -*-


import itertools


if __name__ == "__main__":
    """Day17:  Combinations"""
    
    available_containers = [43,
3,
4,
10,
21,
44,
4,
6,
47,
41,
34,
17,
17,
44,
36,
31,
46,
9,
27,
38]
    available_containers.sort()
    
    target_volume = 150
    
    print(available_containers)
    
    num_combos = 0
    for inum in range(3,len(available_containers)+1):
        for trial_list in itertools.combinations(available_containers, inum):
            trial_sum = sum(trial_list)
            if trial_sum == target_volume:
                num_combos += 1
                print("{0}: {1}".format(num_combos, trial_list))
            

    print("Found {0} combos".format(num_combos))
    # part 1 = 1638
    
    
    
    
    
    