network = {
    'A': {
        'Parents': [],
        'CPT': {
            (): 0.2 
            }
        
    },
    'B': {
        'Parents': [],
        'CPT': {
            (): 0.2 
            }
        
    },
    'C': {
        'Parents': [],
        'CPT': {
            (): 0.2 
            }
        
    },
    'D': {
        'Parents': ['B'], #true and false cannot be the same
        'CPT': {
            (True,): 0.2, 
            (False,): 0.3, 
            }
        
    },
    'E': {
        'Parents': ['B'], #true and false cannot be the same
        'CPT': {
            (True,): 0.2, 
            (False,): 0.3, 
            }
        
    },

}


print(sorted(network.keys()))