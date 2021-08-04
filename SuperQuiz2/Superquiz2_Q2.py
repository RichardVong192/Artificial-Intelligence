def depth(expression):
    if type(expression) is str or type(expression) is int:
        return 0
    else:
        return 1 + max(depth(expression[1]), depth(expression[2]))
        


expression = 12
print(depth(expression))

print("=" * 20)

expression = 'weight'
print(depth(expression))

print("=" * 20)

expression = ['add', 12, 'x']
print(depth(expression))

print("=" * 20)

expression = ['add', ['add', 22, 'y'], 'x']
print(depth(expression))

print("=" * 20)

expression = ['+', ['*', 2, 'i'], ['*', -3, 'x']]
print(depth(expression))
