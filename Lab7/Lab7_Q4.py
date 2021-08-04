import random
from itertools import combinations 

def greedy_descent_with_random_restart(random_state, neighbours, cost):
     state = random_state()                                 #first state obtained by calling ramdom_state()
     while True:
          gd = greedy_descent(state, neighbours, cost)
          for i in gd:                                      #print each state it goes through, so loop through it
               print(i)
          if cost(gd[-1]) == 0:                             #global min = 0, so print restart and reinitalise random state
               break
          print("RESTART")
          state = random_state()
     return None


def greedy_descent(initial_state, neighbours, cost):
     c = cost(initial_state)
     state = initial_state
     aList = [state]
     
     while True:
          #get min based off of cost of each neighbour
          state = min(list(neighbours(state) + [state]), key = lambda x: cost(x))
          if cost(state) < c:
               c = cost(state)
               aList.append(state)
          else: #if the cost goes above local min, then you stop (like a parabola)
               break
     return aList

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


N = 6
random.seed(0)

def random_state():
     return tuple(random.sample(range(1,N+1), N))   

greedy_descent_with_random_restart(random_state, neighbours, cost)

print("=====================")

N = 8
random.seed(0)

greedy_descent_with_random_restart(random_state, neighbours, cost)