/* tear rate related clauses */
normal_tear_rate(RATE) :- RATE >= 5.
low_tear_rate(RATE) :- RATE < 5.

/* age-related clauses */
young(AGE) :- AGE < 45.

/*when patient is young, has normal tear rate and has astigmatic then it should recommend hard_lense*/
diagnosis(hard_lenses, Age, Astigmatic, TearRate) :- normal_tear_rate(TearRate), Astigmatic == yes, young(Age).

/*when patient is young, has normal tear rate and does not have astigmatic then it should recommend soft_lense*/
diagnosis(soft_lenses, Age, Astigmatic, TearRate) :- normal_tear_rate(TearRate), Astigmatic == no, young(Age).

/*if patient has low tear rate then no matter the age or has Astigmatic or not just recommend no lense*/
diagnosis(no_lenses, Age, Astigmatic, TearRate) :- low_tear_rate(TearRate).


test_answer :-
    diagnosis(X, 45, no, 4),
    writeln(X).
