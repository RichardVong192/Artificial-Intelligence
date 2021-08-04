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
    'A': {
        'Parents': [],
        'CPT': {
            (): 0.2
            }},
}

answer = query(network, 'A', {})
print("P(A=true) = {:.5f}".format(answer[True]))
print("P(A=false) = {:.5f}".format(answer[False]))

print("=" * 20)

network = {
    'A': {
        'Parents': [],
        'CPT': {
            (): 0.1
            }},
            
    'B': {
        'Parents': ['A'],
        'CPT': {
            (True,): 0.8,
            (False,): 0.7,
            }},
    }
 
answer = query(network, 'B', {'A': False})
print("P(B=true|A=false) = {:.5f}".format(answer[True]))
print("P(B=false|A=false) = {:.5f}".format(answer[False]))

print("=" * 20)

network = {
    'A': {
        'Parents': [],
        'CPT': {
            (): 0.1
            }},
            
    'B': {
        'Parents': ['A'],
        'CPT': {
            (True,): 0.8,
            (False,): 0.7,
            }},
    }
 
answer = query(network, 'B', {})
print("P(B=true) = {:.5f}".format(answer[True]))
print("P(B=false) = {:.5f}".format(answer[False]))

print("=" * 20)

network = {
    'Burglary': {
        'Parents': [],
        'CPT': {
            (): 0.001
            }},
            
    'Earthquake': {
        'Parents': [],
        'CPT': {
            (): 0.002,
            }},
    'Alarm': {
        'Parents': ['Burglary','Earthquake'],
        'CPT': {
            (True,True): 0.95,
            (True,False): 0.94,
            (False,True): 0.29,
            (False,False): 0.001,
            }},

    'John': {
        'Parents': ['Alarm'],
        'CPT': {
            (True,): 0.9,
            (False,): 0.05,
            }},

    'Mary': {
        'Parents': ['Alarm'],
        'CPT': {
            (True,): 0.7,
            (False,): 0.01,
            }},
    }

answer = query(network, 'Burglary', {'John': True, 'Mary': True})
print("Probability of a burglary when both\n"
      "John and Mary have called: {:.3f}".format(answer[True])) 