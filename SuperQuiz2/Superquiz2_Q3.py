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
        operators = bindings.get(expression[0]) #this is a function
        expression1 = evaluate(expression[1], bindings) #evaluate each expression
        expression2 = evaluate(expression[2], bindings) #evaluate each expression
        return operators(expression1, expression2) #use the function here

bindings = {}
expression = 12
print(evaluate(expression, bindings))

print("=" * 20)

bindings = {'x':5, 'y':10, 'time':15}
expression = 'y'
print(evaluate(expression, bindings))

print("=" * 20)

bindings = {'x': 5, 'y': 10, 'time': 15, 'add': lambda x, y: x + y}
expression = ['add', 12, 'x']
print(evaluate(expression, bindings))

print("=" * 20)

bindings = dict(x = 5, y = 10, blah = 15, add = operator.add)
expression = ['add', ['add', 22, 'y'], 'x']
print(evaluate(expression, bindings))

print("=" * 20)