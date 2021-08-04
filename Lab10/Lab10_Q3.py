def construct_perceptron(weights, bias):
    """Returns a perceptron function using the given paramers."""
    def perceptron(input):
        result = 0
        for i in range(len(weights)):
            result += weights[i] * input[i]
        result += bias
        return 1 if result >= 0 else 0
        
    return perceptron # this line is fine


weights = [2, -4]
bias = 0
perceptron = construct_perceptron(weights, bias)

print(perceptron([1, 1]))
print(perceptron([2, 1]))
print(perceptron([3, 1]))
print(perceptron([-1, -1]))

print("==" * 20)

weights = [1.5, -2.25]
bias = -3.75
perceptron = construct_perceptron(weights, bias)

print(perceptron([1, -4]))
print(perceptron([0, -5]))
print(perceptron([-3, 3]))
print(perceptron([-1, -1]))