import random
import operator


def evaluate(expression, bindings):
    """
    Takes an expression and a dictionary of bindings and 
    returns an integer that is the value of the expression
    """
    if type(expression) == int:
        return expression
    elif type(expression) == str:
        return bindings.get(expression)
    else:  # expression is a list
        operators = bindings.get(expression[0])  # this is a function
        expression1 = evaluate(expression[1], bindings)  # evaluate each expression
        expression2 = evaluate(expression[2], bindings)  # evaluate each expression
        return operators(expression1, expression2)  # use the function here


def random_expression(function_symbols, leaves, max_depth):
    if max_depth == 0:  # max depth is 0
        return random.choice(leaves)
    elif random.randint(0, 1) == 0:  # toss coin
        return random.choice(leaves)
    else:
        return [random.choice(function_symbols), random_expression(function_symbols, leaves, max_depth - 1),
                random_expression(function_symbols, leaves, max_depth - 1)]


def generate_rest(initial_sequence, expression, length):
    """
    Returns a list of integers with the specified length that is 
    the continuation of the initial list according to the given expression
    """
    result = []
    for index in range(length):
        i = len(initial_sequence)  # the index of the first number in the generated sequence
        x = initial_sequence[i - 2]  # X and Y set to the last two elements of the initial sequence
        y = initial_sequence[i - 1]
        bindings = {'i': i, 'x': x, 'y': y, '+': operator.add, '*': operator.mul, '-': operator.sub}
        value = evaluate(expression, bindings)
        initial_sequence.append(value)
        result.append(value)
    return result


def predict_rest(sequence):
    length = len(sequence) - 2
    initial_sequence = sequence[:2]
    expression = random_expression(['+', '-', '*'], ['x', 'y', 'i', -2, -1, 0, 1, 2], 3)
    value = generate_rest(initial_sequence.copy(), expression, length)

    while value != sequence[2:]:
        expression = random_expression(['+', '-', '*'], ['x', 'y', 'i', -2, -1, 0, 1, 2], 3)
        value = generate_rest(initial_sequence.copy(), expression, length)

    return generate_rest(sequence, expression, 5)


sequence = [0, 1, 2, 3, 4, 5, 6, 7]
print(predict_rest(sequence))

print("=" * 30)

sequence = [0, 2, 4, 6, 8, 10, 12, 14]
print(predict_rest(sequence))

print("=" * 30)

sequence = [31, 29, 27, 25, 23, 21]
print(predict_rest(sequence))

print("=" * 30)

sequence = [0, 1, 4, 9, 16, 25, 36, 49]
print(predict_rest(sequence))

print("=" * 30)

sequence = [3, 2, 3, 6, 11, 18, 27, 38]
print(predict_rest(sequence))

print("=" * 30)

sequence =  [0, 1, 1, 2, 3, 5, 8, 13]
print(predict_rest(sequence))

print("=" * 30)

sequence = [0, -1, 1, 0, 1, -1, 2, -1]
print(predict_rest(sequence))

print("=" * 30)

sequence = [1, 3, -5, 13, -31, 75, -181, 437]
print(predict_rest(sequence))

print("=" * 30)
