import itertools

def joint_prob(network, assignment):
    joint_prob = 1
    for var in network:
        this = network[var]
        parents = this["Parents"]   #used to get info from the network
        CPT = this["CPT"]           #used to get info from the network
        parent_assignments = []     #used to get info from the network
        if len(parents) > 0:
            for parents in parents:
                parent_assignments.append(assignment[parents])
        if var in assignment:
            if assignment[var]: #if true
                joint_prob *= CPT[tuple(parent_assignments)]
            else:               #if false
                joint_prob *= 1 - CPT[tuple(parent_assignments)]
    return joint_prob

def query(network, query_var, evidence):
    result = {True: 0, False: 0}
    
    hidden_vars = network.keys() - evidence.keys() - {query_var}
    for values in itertools.product((True, False), repeat=len(hidden_vars)):    #all permutations of the variables
        hidden_assignments = {var:val for var,val in zip(hidden_vars, values)}  #assigns one permutation to a dictionary
        
        assignment = {**hidden_assignments, **evidence} #combining hidden assignment and evidence into a single assignment
        for value in [True, False]:                 #Iterate over true and false
            assignment[query_var] = value           #Make assignment for query var as true/false
            prob = joint_prob(network, assignment)  #Find prob of that assignment
            result[value] += prob                   #Add to the result for True/False
    
    total = sum(result.values())
    return (result[False] / total, result[True]/total)



network = {
    'Disease': {
        'Parents': [],
        'CPT': {
            (): 0.00001
            }},
            
    'Test': {
        'Parents': ['Disease'],
        'CPT': {
            (True,): 0.99,
            (False,): 0.01,
            }},
}


answer = query(network, 'Disease', {'Test': True})
print("The probability of having the disease\n"
      "if the test comes back positive: {:.8f}"
      .format(answer[True]))


answer = query(network, 'Disease', {'Test': False})
print("The probability of having the disease\n"
      "if the test comes back negative: {:.8f}"
      .format(answer[True]))