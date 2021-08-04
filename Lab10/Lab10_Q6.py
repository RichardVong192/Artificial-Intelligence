def construct_perceptron(weights, bias):
    """Returns a perceptron function using the given paramers."""
    def perceptron(input):
        result = 0
        for i in range(len(weights)):
            result += weights[i] * input[i]
        result += bias
        return 1 if result >= 0 else 0
        
    return perceptron # this line is fine

def learn_perceptron_parameters(weights, bias, training_examples, learning_rate, max_epochs):
    """
    @param weights: an list of initial weights of length n
    @param bias: initial bias
    @param training_examples:
    @param learning_rate: a positive number representing eta
    @param max_epochs: the maximum number to iterate through all thr training examples
    """
    perceptron = construct_perceptron(weights, bias)
    # xn is inputs
    # t stands for target value, you will be give a value to see if machine did it right as this is supervised learning
    # wj = wj + n * xj (t-y) next weight += learning rate (eta) * input * (expected - result)
    # bias = bias + n * (t-y)
    for epoch in range(max_epochs):
        for xn, t in training_examples:
            y = perceptron(xn)
            if t != y:
                for j, wj in enumerate(weights):
                    weights[j] = wj + learning_rate * xn[j] * (t - y)
                bias += learning_rate * (t - y)
                perceptron = construct_perceptron(weights, bias)
    return [weights, bias]

#def learn_perceptron_parameters(weights, bias, training_examples, learning_rate, max_epochs):
    #has_learned = 0
    
    #for i in range(max_epochs):
        #if has_learned:
            #break
        #has_learned = 1
        
        #for pair,expected_result in training_examples:
            #perceptron = construct_perceptron(weights,bias)
            #output = perceptron(pair)
            #if output != expected_result:
                #has_learned = 0
                #for i in range(len(weights)):
                    #weights[i] += learning_rate*pair[i]*(expected_result-output)
                #bias += learning_rate*(expected_result - output)    
    #result = [weights, bias]
    #return result


weights = [2, -4]
bias = 0
learning_rate = 0.5
examples = [
  ((0, 0), 0),
  ((0, 1), 0),
  ((1, 0), 0),
  ((1, 1), 1),
  ]
max_epochs = 50

weights, bias = learn_perceptron_parameters(weights, bias, examples, learning_rate, max_epochs)
print(f"Weights: {weights}")
print(f"Bias: {bias}\n")

perceptron = construct_perceptron(weights, bias)

print(perceptron((0,0)))
print(perceptron((0,1)))
print(perceptron((1,0)))
print(perceptron((1,1)))
print(perceptron((2,2)))
print(perceptron((-3,-3)))

print("==" * 20)

weights = [2, -4]
bias = 0
learning_rate = 0.5
examples = [
  ((0, 0), 0),
  ((0, 1), 1),
  ((1, 0), 1),
  ((1, 1), 0),
  ]
max_epochs = 50

weights, bias = learn_perceptron_parameters(weights, bias, examples, learning_rate, max_epochs)
print(f"Weights: {weights}")
print(f"Bias: {bias}\n")