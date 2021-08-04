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


print(euclidean_distance([0, 3, 1, -3, 4.5],[-2.1, 1, 8, 1, 1]))

print("=" * 30)

print(majority_element([0, 0, 0, 0, 0, 1, 1, 1]))
print(majority_element("ababc") in "ab")