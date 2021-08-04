network = {
    'A': {
        'Parents': [],
        'CPT': {
            (): 0.1
            }},
    'B': {
        'Parents': ['A'], #doesnt matter whether false or true, they are the same thus independent of A
        'CPT': {
            (False,): 0.2,
            (True,): 0.2
            }},
            
    'C': {
        'Parents': ['A'],
        'CPT': {
            (False,): 0.5,
            (True,): 0.5
            }},
}

print(sorted(network.keys()))