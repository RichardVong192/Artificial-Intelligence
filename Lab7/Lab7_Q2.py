from itertools import combinations 

def n_queens_cost(state):
    """
    takes a state (a total assignment) for an n-queen problem and returns the 
    number conflicts for that state. We define the number of conflicts to be 
    the number of unordered pairs of queens (objects) that threaten (attack) 
    each other.
    """
    
    total = 0
    for (x, y) in combinations(range(len(state)), 2):
        #check index against actual value of the index if they match (the change in the two must be 1)
        if abs(x-y) == abs(state[x] - state[y]): 
            total += 1
    return total
    
cost = n_queens_cost


print(cost((1, 2)))

print(cost((1, 3, 2)))

print(cost((1, 2, 3)))

print(cost((1,)))

print(cost((1, 2, 3, 4, 5, 6, 7, 8)))

print(cost((2, 3, 1, 4)))