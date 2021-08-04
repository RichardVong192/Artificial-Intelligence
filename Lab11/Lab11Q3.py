from math import inf

pruned_tree = [
    2, [-1], [1], 4
    ]
    

pruning_events = [
    # (alpha, beta),
    (2, -1), # alpha >= beta so prune and 2 is returned as node value
    (2, 1), #alpha >= beta so prune and 1 is returned as the node value
    ]

#alpha = highest-value choice found for MAX high up in the tree, initially -inf
#beta = lowest-value choice found for MIN higher up in the tree, initially +inf
#Pass current value of alpha and beta down to child nodes during search
#Update values of alpha and beta during search
#Prune remaining branches at a node when alpha >= beta