import csv

def posterior(prior, likelihood, observation):
    """Returns the prosterior prob of the class variable bing true, give the observation that is it returns."""
    prosterior_prob = 0
    prob_true = prior
    prob_false = 1 - prior
    #likelihood = input
    #obsevation = class

    for i in range(len(observation)):
        if observation[i] == True:              #if true we are happy with the prob and update accordingly
            prob_true *= likelihood[i][1]       
            prob_false *= likelihood[i][0]
        else:                                   #if false we are not happy and we want to take the inverse of both of them
            prob_true *= 1 - likelihood[i][1]   #Marginalisation (dividing my multiplying by the inverse)
            prob_false *= 1 - likelihood[i][0]  
    prosterior_prob = prob_true / (prob_true + prob_false)
    return prosterior_prob

def learn_prior(file_name, pseudo_count=0):
    """
    takes the file name of the training set and an optional pseudo-count 
    parameter and returns a real number that is the prior probability of spam being true.
    """
    true_count = pseudo_count
    false_count = pseudo_count
    with open(file_name) as in_file:
            training_examples = [tuple(row) for row in csv.reader(in_file)]
    
    for i in training_examples:
        if i[-1] == str("1"):
            true_count += 1
        elif i[-1] == str("0"):
            false_count += 1

    result = true_count / (true_count + false_count)
    return result

def learn_likelihood(file_name, pseudo_count=0):
    with open(file_name) as in_file:
            training_examples = [tuple(row) for row in csv.reader(in_file)]
            
    likelihood = []
    spam_true = []
    spam_false = []
    for example in training_examples[1:]:
        if example[12] == str("1"):
            spam_true.append(example)
        else:
            spam_false.append(example)
    
    number_of_variables = len(training_examples[0])-1
    for var in range(number_of_variables):
        
        true_count = 0      #set count to 0
        for row in spam_true:    #Calculate likelihood when spam is true
            if row[var] == str("1"):   #Variable true when spam is true
                true_count += 1
        likelihoodTrue = (true_count + pseudo_count) / (len(spam_true) + 2 * pseudo_count)
        
        true_count = 0          #set count to 0
        for row in spam_false:   #And calculate likelihood when spam is false
            if row[var] == str("1"):    #Variable true when spam is false
                true_count += 1
        likelihoodFalse = (true_count + pseudo_count) / (len(spam_false) + 2 * pseudo_count)
    
        likelihood.append((likelihoodFalse, likelihoodTrue))
    return likelihood

def nb_classify(prior, likelihood, input_vector):
    posteriorProb = posterior(prior, likelihood, input_vector)
    is_spam = "Not Spam"
    
    if posteriorProb < 0.50:    #If prob is less than 50% than its probably not spam
        posteriorProb = 1 - posteriorProb
    else:                       #Else if it is more than 50% than its probably spam
        is_spam = "Spam"
    return (is_spam, posteriorProb)
    
    

prior = learn_prior("spam-labelled.csv")
likelihood = learn_likelihood("spam-labelled.csv")

input_vectors = [
    (1,1,0,0,1,1,0,0,0,0,0,0),
    (0,0,1,1,0,0,1,1,1,0,0,1),
    (1,1,1,1,1,0,1,0,0,0,1,1),
    (1,1,1,1,1,0,1,0,0,1,0,1),
    (0,1,0,0,0,0,1,0,1,0,0,0),
    ]

predictions = [nb_classify(prior, likelihood, vector) 
               for vector in input_vectors]

for label, certainty in predictions:
    print("Prediction: {}, Certainty: {:.5f}"
          .format(label, certainty))
    
print("=" * 30)

prior = learn_prior("spam-labelled.csv", pseudo_count=1)
likelihood = learn_likelihood("spam-labelled.csv", pseudo_count=1)

input_vectors = [
    (1,1,0,0,1,1,0,0,0,0,0,0),
    (0,0,1,1,0,0,1,1,1,0,0,1),
    (1,1,1,1,1,0,1,0,0,0,1,1),
    (1,1,1,1,1,0,1,0,0,1,0,1),
    (0,1,0,0,0,0,1,0,1,0,0,0),
    ]

predictions = [nb_classify(prior, likelihood, vector) 
               for vector in input_vectors]

for label, certainty in predictions:
    print("Prediction: {}, Certainty: {:.5f}"
          .format(label, certainty))