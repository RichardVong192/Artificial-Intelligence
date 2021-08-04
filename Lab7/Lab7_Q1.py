def n_queens_neighbours(state):
    """
    Takes a state (total assignment) for an n-queen problem and returns a sorted 
    list of states that are the neighbours of the current assignment. 
    A neighbour is obtained by swapping the position of two numbers in the given permutation.
    """
    result = []
    for i in range(len(state)):
        for j in range (i+1, len(state)):
            perm = list(state)
            temp = state[i]
            perm[i] = perm[j]
            perm[j] = temp
            result.append(tuple(perm))
    return sorted(result)
neighbours = n_queens_neighbours
    

print(neighbours((1, 2)))

print(neighbours((1, 3, 2)))

print(neighbours((1, 2, 3)))

print(neighbours((1,))) 
