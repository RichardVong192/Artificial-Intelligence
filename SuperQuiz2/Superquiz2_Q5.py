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
    else: #expression is a list
        operators = bindings.get(expression[0])         #this is a function
        expression1 = evaluate(expression[1], bindings) #evaluate each expression
        expression2 = evaluate(expression[2], bindings) #evaluate each expression
        return operators(expression1, expression2)      #use the function here

def generate_rest(initial_sequence, expression, length):
    """
    Returns a list of integers with the specified length that is 
    the continuation of the initial list according to the given expression
    """ 
    result = []
    
    for index in range(length):
        i = len(initial_sequence)   #the index of the first number in the generated sequence
        x = initial_sequence[i-2]    #X and Y set to the last two elements of the initial sequence
        y = initial_sequence[i-1]
        bindings = {'i': i, 'x': x, 'y': y, '+': operator.add, '*': operator.mul, '-': operator.sub}
        value = evaluate(expression, bindings)
        initial_sequence.append(value)
        result.append(value)
        
    return result

initial_sequence = [0, 1, 2]
expression = 'i' 
length_to_generate = 5
print(generate_rest(initial_sequence, 
                    expression,
                    length_to_generate))

print("==" * 20)

# no particular pattern, just an example expression
initial_sequence = [-1, 1, 367]
expression = 'i' 
length_to_generate = 4
print(generate_rest(initial_sequence,
                    expression,
                    length_to_generate))

print("==" * 20)

initial_sequence = [4, 6, 8, 10]
expression = ['*', ['+', 'i', 2], 2]
length_to_generate = 5
print(generate_rest(initial_sequence, 
                    expression, 
                    length_to_generate))

print("==" * 20)

initial_sequence = [4, 6, 8, 10]
expression = ['+', 2, 'y']
length_to_generate = 5
print(generate_rest(initial_sequence, 
                    expression, 
                    length_to_generate))

print("==" * 20)

initial_sequence = [0, 1]
expression = 'x'
length_to_generate = 6
print(generate_rest(initial_sequence, 
                    expression, 
                    length_to_generate))

print("==" * 20)

# Fibonacci sequence
initial_sequence = [0, 1]
expression = ['+', 'x', 'y']
length_to_generate = 5
print(generate_rest(initial_sequence, 
                    expression, 
                    length_to_generate))

print("==" * 20)

initial_sequence = [367, 367, 367]
expression = 'y'
length_to_generate = 5
print(generate_rest(initial_sequence, 
                    expression, 
                    length_to_generate))

print("==" * 20)

# no pattern, just a demo
initial_sequence = [0, 1, 2]
expression = -1 
length_to_generate = 5
print(generate_rest(initial_sequence, 
                    expression, 
                    length_to_generate))

print("==" * 20)

initial_sequence = [0, 1, 2]
expression = 'i'
length_to_generate = 0
print(generate_rest(initial_sequence, 
                    expression, 
                    length_to_generate))