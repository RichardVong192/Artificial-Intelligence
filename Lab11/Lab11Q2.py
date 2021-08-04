def max_value(tree):
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


def max_action_value(game_tree):
    value = float('-inf')
    action = -99
    if type(game_tree) == int:
        return None, game_tree

    for i in range(len(game_tree)):
        temp = min_value(game_tree[i])
        if temp > value:
            value = temp
            action = i
            
    return action, value

def min_action_value(game_tree):
    value = float('inf')
    action = -99
    if type(game_tree) == int:
        return None, game_tree

    for i in range(len(game_tree)):
        temp = max_value(game_tree[i])
        if temp < value:
            value = temp
            action = i
            
    return action, value



game_tree = [2, [-3, 1], 4, 1]

action, value = min_action_value(game_tree)
print("Best action if playing min:", action)
print("Best guaranteed utility:", value)
print()
action, value = max_action_value(game_tree)
print("Best action if playing max:", action)
print("Best guaranteed utility:", value)

print("==" * 20)

game_tree = 3

action, value = min_action_value(game_tree)
print("Best action if playing min:", action)
print("Best guaranteed utility:", value)
print()
action, value = max_action_value(game_tree)
print("Best action if playing max:", action)
print("Best guaranteed utility:", value)

print("==" * 20)

game_tree = [1, 2, [3]]

action, value = min_action_value(game_tree)
print("Best action if playing min:", action)
print("Best guaranteed utility:", value)
print()
action, value = max_action_value(game_tree)
print("Best action if playing max:", action)
print("Best guaranteed utility:", value)
