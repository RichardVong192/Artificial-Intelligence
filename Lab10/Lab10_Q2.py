import math

def euclidean_distance(v1, v2):
    summ = 0
    for a, b in zip(v1, v2):
        expression = (a - b) ** 2
        summ += expression
    result = math.sqrt(summ)
    
    return result

def majority_element(labels):
    maxx = 0
    result = labels[0]
    for i in labels:
        freq = labels.count(i)
        if freq > maxx:
            maxx = freq
            result = i
    return result

def knn_predict(input, examples, distance, combine, k):
    results = []
    examplesCopy = examples.copy() #You copy cause the test cases are recursive
    examplesCopy.sort(key = lambda y: distance(input, y[0])) #Sorting list based on distance of input and value of the first item of every element in the list
    for i in range(k): #loop through k neigbours
        item = examplesCopy.pop(0)  #pop item
        results.append(item[1]) #append the element symbol thingy 
        last_pos = item[0]
        
    while (examplesCopy and distance(input, last_pos) == distance(input, examplesCopy[0][0])):  #If after selecting k nearest neighbours, the distance to the farthest selected neighbour
        item = examplesCopy.pop(0)                                                        #and the distance to the nearest unselected neighbour are the same, more neighbours must 
        results.append(item[1])                                                       #be selected until these two distances become different or all the examples are selected
        last_pos = item[0]
    
    return combine(results)



examples = [
    ([2], '-'),
    ([3], '-'),
    ([5], '+'),
    ([8], '+'),
    ([9], '+'),
]

distance = euclidean_distance
combine = majority_element

for k in range(1, 6, 2):
    print("k =", k)
    print("x", "prediction")
    for x in range(0,10):
        print(x, knn_predict([x], examples, distance, combine, k))
    print()

print("==============")

# using knn for predicting numeric values

examples = [
    ([1], 5),
    ([2], -1),
    ([5], 1),
    ([7], 4),
    ([9], 8),
]

def average(values):
    return sum(values) / len(values)

distance = euclidean_distance
combine = average

for k in range(1, 6, 2):
    print("k =", k)
    print("x", "prediction")
    for x in range(0,10):
        print("{} {:4.2f}".format(x, knn_predict([x], examples, distance, combine, k)))
    print()