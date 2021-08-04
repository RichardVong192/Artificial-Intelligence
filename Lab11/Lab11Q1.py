def  max_value(tree):
    result = float('-inf')
    if type(tree) == int:
        return tree
    for i in range(len(tree)):
        result = max(result, min_value(tree[i]))
    return result
    

def min_value(tree):
    result = float('inf')
    if type(tree) == int:
        return tree
    for i in range(len(tree)):
        result = min(result, max_value(tree[i]))
    return result


game_tree = 3

print("Root utility for minimiser:", min_value(game_tree))
print("Root utility for maximiser:", max_value(game_tree))

print("==" * 20)

game_tree = [1, 2, 3]

print("Root utility for minimiser:", min_value(game_tree))
print("Root utility for maximiser:", max_value(game_tree))

print("==" * 20)

game_tree = [1, 2, [3]]

print(min_value(game_tree))
print(max_value(game_tree))

print("==" * 20)

game_tree = [[1, 2], [3]]

print(min_value(game_tree))
print(max_value(game_tree))