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

def cost(x):
     return x**2

def neighbours(x):
     return [x - 1, x + 1]

for state in greedy_descent(4, neighbours, cost):
     print(state)

print("============")

for state in greedy_descent(-6.75, neighbours, cost):
     print(state)
     
print("============")

def cost(x):
     return -x**2

def neighbours(x):
     return [x - 1, x + 1] if abs(x) < 5 else []

for state in greedy_descent(0, neighbours, cost):
     print(state)