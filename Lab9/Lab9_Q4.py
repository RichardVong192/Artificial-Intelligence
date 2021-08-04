import csv

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





likelihood = learn_likelihood("spam-labelled.csv")
print(len(likelihood))
print([len(item) for item in likelihood])

print("=" * 20)

likelihood = learn_likelihood("spam-labelled.csv")

print("P(X1=True | Spam=False) = {:.5f}".format(likelihood[0][False]))
print("P(X1=False| Spam=False) = {:.5f}".format(1 - likelihood[0][False]))
print("P(X1=True | Spam=True ) = {:.5f}".format(likelihood[0][True]))
print("P(X1=False| Spam=True ) = {:.5f}".format(1 - likelihood[0][True]))

print("=" * 20)

likelihood = learn_likelihood("spam-labelled.csv", pseudo_count=1)

print("With Laplacian smoothing:")
print("P(X1=True | Spam=False) = {:.5f}".format(likelihood[0][False]))
print("P(X1=False| Spam=False) = {:.5f}".format(1 - likelihood[0][False]))
print("P(X1=True | Spam=True ) = {:.5f}".format(likelihood[0][True]))
print("P(X1=False| Spam=True ) = {:.5f}".format(1 - likelihood[0][True]))