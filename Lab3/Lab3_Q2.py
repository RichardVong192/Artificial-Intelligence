import re

def clauses(knowledge_base):
    """Takes the string of a knowledge base; returns an iterator for pairs
    of (head, body) for propositional definite clauses in the
    knowledge base. Atoms are returned as strings. The head is an atom
    and the body is a (possibly empty) list of atoms.

    -- Kourosh Neshatian - 31 Jul 2019

    """
    ATOM   = r"[a-z][a-zA-z\d_]*"
    HEAD   = rf"\s*(?P<HEAD>{ATOM})\s*"
    BODY   = rf"\s*(?P<BODY>{ATOM}\s*(,\s*{ATOM}\s*)*)\s*"
    CLAUSE = rf"{HEAD}(:-{BODY})?\."
    KB     = rf"^({CLAUSE})*\s*$"

    assert re.match(KB, knowledge_base)

    for mo in re.finditer(CLAUSE, knowledge_base):
        yield mo.group('HEAD'), re.findall(ATOM, mo.group('BODY') or "")
        
def forward_deduce(kb):
    """Takes the string of a knowledge base containing propositional definite clauses and returns a
     (complete) set of atoms (strings) that can be derived (to be true) from the knowledge base
     
     """
    list_clauses = list(clauses(kb)) #construct a new clauses list using the clause object
    aSet = set()
    
    #Add single clauses
    for clause in list_clauses:
        if len(clause[1]) == 0:
            aSet.add(clause[0])
            
    stillAddingThingsToSet = True
    
    #Loop through clauses checking and adding when body pair is valid
    while stillAddingThingsToSet:
        stillAddingThingsToSet = False
        for clause in list_clauses:
            clauseSet = set(clause[1])
            if clauseSet.issubset(aSet) and clause[0] not in aSet: #Need to heck if already in set or not, otherwise it keeps adding it to the set for no reason
                aSet.add(clause[0])
                stillAddingThingsToSet = True
                
    return aSet
                    

kb = """
a :- b.
b.
"""

print(", ".join(sorted(forward_deduce(kb))))

print("=========================")
kb = """
good_programmer :- correct_code.
correct_code :- good_programmer.
"""

print(", ".join(sorted(forward_deduce(kb))))

print("==========================")
kb = """
a :- b, c.
b :- d, e.
b :- g, e.
c :- e.
d.
e.
f :- a,
     g.
"""

print(", ".join(sorted(forward_deduce(kb))))