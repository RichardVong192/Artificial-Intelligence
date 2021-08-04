from math import inf

pruned_tree = [
    0, [-2, 1], 5
    ]
    

pruning_events = [
    # (alpha, beta),
    (1, 0)
    ]


#alpha = highest-value choice found for MAX high up in the tree, initially -inf
#beta = lowest-value choice found for MIN higher up in the tree, initially +inf
#Pass current value of alpha and beta down to child nodes during search
#Update values of alpha and beta during search
#Prune remaining branches at a node when alpha >= beta