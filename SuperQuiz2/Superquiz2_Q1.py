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
    
    

function_symbols = ['f', '+']
leaf_symbols = ['x', 'y']
expression = 1

print(is_valid_expression(expression, function_symbols, leaf_symbols))

print("=" * 20)

function_symbols = ['f', '+']
leaf_symbols = ['x', 'y']
expression = 'y'

print(is_valid_expression(
        expression, function_symbols, leaf_symbols))

print("=" * 20)

function_symbols = ['f', '+']
leaf_symbols = ['x', 'y']
expression = 2.0

print(is_valid_expression(
        expression, function_symbols, leaf_symbols))

print("=" * 20)

function_symbols = ['f', '+']
leaf_symbols = ['x', 'y']
expression = ['f', 123, 'x']

print(is_valid_expression(
        expression, function_symbols, leaf_symbols))

print("=" * 20)

function_symbols = ['f', '+']
leaf_symbols = ['x', 'y']
expression = ['f', ['+', 0, -1], ['f', 1, 'x']]

print(is_valid_expression(
        expression, function_symbols, leaf_symbols))

print("=" * 20)

function_symbols = ['f', '+']
leaf_symbols = ['x', 'y']
expression = ['+', ['f', 1, 'x'], -1]

print(is_valid_expression(
        expression, function_symbols, leaf_symbols))

print("=" * 20)

function_symbols = ['f', '+']
leaf_symbols = ['x', 'y', -1, 0, 1]
expression = ['f', 0, ['f', 0, ['f', 0, ['f', 0, 'x']]]]

print(is_valid_expression(
        expression, function_symbols, leaf_symbols))

print("=" * 20)

function_symbols = ['f', '+']
leaf_symbols = ['x', 'y']
expression = 'f'

print(is_valid_expression(
        expression, function_symbols, leaf_symbols))

print("=" * 20)

function_symbols = ['f', '+']
leaf_symbols = ['x', 'y']
expression = ['f', 1, 0, -1]

print(is_valid_expression(
        expression, function_symbols, leaf_symbols))

print("=" * 20)

function_symbols = ['f', '+']
leaf_symbols = ['x', 'y']
expression = ['x', 0, 1]

print(is_valid_expression(
        expression, function_symbols, leaf_symbols))

print("=" * 20)

function_symbolsfunction_symbols = ['f', '+']
leaf_symbols = ['x', 'y']
expression = ['g', 0, 'y']

print(is_valid_expression(
        expression, function_symbols, leaf_symbols))