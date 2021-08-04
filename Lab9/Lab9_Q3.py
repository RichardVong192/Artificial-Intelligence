import csv

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



prior = learn_prior("spam-labelled.csv")
print("Prior probability of spam is {:.5f}.".format(prior))

print("=" * 20)

prior = learn_prior("spam-labelled.csv")
print("Prior probability of not spam is {:.5f}.".format(1 - prior))

print("=" * 20)

prior = learn_prior("spam-labelled.csv", pseudo_count = 1)
print(format(prior, ".5f"))

print("=" * 20)

prior = learn_prior("spam-labelled.csv", pseudo_count = 2)
print(format(prior, ".5f"))

print("=" * 20)

prior = learn_prior("spam-labelled.csv", pseudo_count = 10)
print(format(prior, ".5f"))

print("=" * 20)

prior = learn_prior("spam-labelled.csv", pseudo_count = 100)
print(format(prior, ".5f"))

print("=" * 20)

prior = learn_prior("spam-labelled.csv", pseudo_count = 1000)
print(format(prior, ".5f"))