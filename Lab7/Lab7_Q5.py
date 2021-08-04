def roulette_wheel_select(population, fitness, r):
    T = sum(fitness(x) for x in population) #sum the fitness of all individuals 
    N = r * T                               #generate a random number N between 1 and T (they give us r so we multiply by T)
    total = 0
    for i in population:
        total += fitness(i)
        if total > N:                       #Return invididual whoes fitness level added to running total is LARGER than N
            return i

population = ['a', 'b']

def fitness(x):
    return 1 # everyone has the same fitness

for r in [0, 0.33, 0.49999, 0.5, 0.75, 0.99999]:
    print(roulette_wheel_select(population, fitness, r))

print("=" * 20)

population = [0, 1, 2]

def fitness(x):
    return x

for r in [0, 0.33, 0.34, 0.5, 0.75, 0.99]:
    print(roulette_wheel_select(population, fitness, r))