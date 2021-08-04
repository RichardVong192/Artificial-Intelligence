network = {
    'X1': {
        'Parents': ['Y'],
        'CPT': {
            (True,): (3/8),   #X1 given Y is true
            (False,): (5/7),  #X1 given Y is false
         }
    },
        
    'X2': {
        'Parents': ['Y'],
        'CPT': {
            (True,): (3/8),  #X2 given Y is true
            (False,): (4/7), #X2 given Y is false
        }
    },

    'X3': {
        'Parents': ['Y'],
        'CPT': {
            (True,): (2/8),   #X3 given y is true ((X3 True+2)/((Y True+2) + (Y False + 2)))
            (False,): (2/7),  #X3 given y is false
        }
    },

    'Y': {
        'Parents': [],
        'CPT': {
            (): ((4+2)/(7+4)),
        }
    },

}


from numbers import Number

# Checking the overall type-correctness of the network
# without checking anything question-specific

assert type(network) is dict
for node_name, node_info in network.items():
    assert type(node_name) is str
    assert type(node_info) is dict
    assert set(node_info.keys()) == {'Parents', 'CPT'}
    assert type(node_info['Parents']) is list
    assert all(type(s) is str for s in node_info['Parents'])
    for assignment, prob in node_info['CPT'].items():
        assert type(assignment) is tuple
        assert isinstance(prob, Number)

print("OK")


for assignment, prob in sorted(network['X1']['CPT'].items()):
    print(assignment, "{:0.2f}".format(prob))