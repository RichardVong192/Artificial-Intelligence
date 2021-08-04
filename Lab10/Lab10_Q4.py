def construct_perceptron(weights, bias):
    """Returns a perceptron function using the given paramers."""
    def perceptron(input):
        result = 0
        for i in range(len(weights)):
            result += weights[i] * input[i]
        result += bias
        return 1 if result >= 0 else 0
        
    return perceptron # this line is fine


def accuracy(classifier, inputs, expected_outputs):
    result = 0
    for index in range(len(inputs)):
        if classifier(inputs[index]) == expected_outputs[index]:
            result += 1
    return result / len(expected_outputs)
    

perceptron = construct_perceptron([-1, 3], 2)
inputs = [[1, -1], [2, 1], [3, 1], [-1, -1]]
targets = [0, 1, 1, 0]

print(accuracy(perceptron, inputs, targets))