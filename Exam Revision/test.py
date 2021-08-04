def joint_prob(network, assignment):
    
    joint_prob = 1
    for var in network:
        this = network[var]
        parents = this["Parents"]
        CPT = this["CPT"]
        parent_assignements = []
        if len(parents) > 0:
            for parent in parents:
                parent_assignements.append(assignment[parent])
            print(parent_assignements)
        if assignment[var]: #if true
            joint_prob *= CPT[tuple(parent_assignements)]
        else:               #if false
            joint_prob *= 1 - CPT[tuple(parent_assignements)]
    return joint_prob

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

p = joint_prob(network, {'A': False, 'B':True})
print("{:.5f}".format(p))