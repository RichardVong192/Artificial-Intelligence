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
            prob_true *= 1 - likelihood[i][1]   #Marginalisation (dividing my multiplying by the inverse
            prob_false *= 1 - likelihood[i][0]  
    prosterior_prob = prob_true / (prob_true + prob_false)
    return prosterior_prob
    


prior = 0.05
likelihood = ((0.001, 0.3),(0.05,0.9),(0.7,0.99))

observation = (True, True, True)

class_posterior_true = posterior(prior, likelihood, observation)
print("P(C=False|observation) is approximately {:.5f}"
      .format(1 - class_posterior_true))
print("P(C=True |observation) is approximately {:.5f}"
      .format(class_posterior_true)) 

print("=" * 20)

prior = 0.05
likelihood = ((0.001, 0.3),(0.05,0.9),(0.7,0.99))

observation = (True, False, True)

class_posterior_true = posterior(prior, likelihood, observation)
print("P(C=False|observation) is approximately {:.5f}"
      .format(1 - class_posterior_true))
print("P(C=True |observation) is approximately {:.5f}"
      .format(class_posterior_true))

print("=" * 20)

prior = 0.05
likelihood = ((0.001, 0.3),(0.05,0.9),(0.7,0.99))

observation = (False, False, True)

class_posterior_true = posterior(prior, likelihood, observation)
print("P(C=False|observation) is approximately {:.5f}"
      .format(1 - class_posterior_true))
print("P(C=True |observation) is approximately {:.5f}"
      .format(class_posterior_true))  