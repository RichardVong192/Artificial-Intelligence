import random

def _check_diversity(expressions, max_depth):
    countDic = {0:0, 1:0, 2:0, 3:0, 4:0}
    for expression in expressions:
        countDic[depth(expression)] += 1
    return all(x >= 100 for x in countDic.values())

def _check_distinctness(expressions):
    a = [str(x) for x in expressions]
    return len(a) >= 1000

def depth(expression):
    if type(expression) is str or type(expression) is int:
        return 0
    else:
        return 1 + max(depth(expression[1]), depth(expression[2]))

def is_valid_expression(object, function_symbols, leaf_symbols):
    """
    Takes an object as its first argument and tests whether it is a valid expression 
    according to our definition of expressions in this assignment. 
    The function returns True if the given object is valid expression, False otherwise
    """
    #if it is an integer
    if type(object) is int: 
        return True
    
    #if it is a leaf symbol
    if object in leaf_symbols: 
        return True
    
    #list has length 3 and first element is in function symbols
    if (type(object) is list and len(object) == 3) and object[0] in function_symbols and is_valid_expression(object[1], function_symbols, leaf_symbols) and is_valid_expression(object[2], function_symbols, leaf_symbols):
        return True
    
    return False


def random_expression(function_symbols, leaves, max_depth):
    if max_depth == 0:              #max depth is 0
        return random.choice(leaves)
    elif random.randint(0, 1) == 0: #toss coin
        return random.choice(leaves)
    else:
        return [random.choice(function_symbols), random_expression(function_symbols, leaves, max_depth-1), random_expression(function_symbols, leaves, max_depth - 1)]








# All the generated expressions must be valid

function_symbols = ['f', 'g', 'h']
constant_leaves =  list(range(-2, 3))
variable_leaves = ['x', 'y', 'i']
leaves = constant_leaves + variable_leaves
max_depth = 4

for _ in range(10000):
    expression = random_expression(function_symbols, leaves, max_depth)
    if not is_valid_expression(expression, function_symbols, leaves):
        print("The following expression is not valid:\n", expression)
        break
else:
    print("OK")
    
print("========================================================")

function_symbols = ['f', 'g', 'h']
leaves = ['x', 'y', 'i'] + list(range(-2, 3))
max_depth = 4

expressions = [random_expression(function_symbols, leaves, max_depth)
               for _ in range(10000)]

# Out of 10000 expressions, at least 1000 must be distinct

print(_check_distinctness(expressions))
    
print("========================================================")

function_symbols = ['f', 'g', 'h']
leaves = ['x', 'y', 'i'] + list(range(-2, 3))
max_depth = 4

expressions = [random_expression(function_symbols, leaves, max_depth)
               for _ in range(10000)]

# Out of 10000 expressions, there must be at least 100 expressions
# of depth 0, 100 of depth 1, ..., and 100 of depth 4.

print(_check_diversity(expressions, max_depth))
    