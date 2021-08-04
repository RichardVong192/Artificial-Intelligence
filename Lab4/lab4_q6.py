/*'yes' if first doll is directly in the second doll */

/* 'yes' if irina is inside natasha */
directlyIn(irina, natasha).
/* 'yes' if natasha is inside olga */
directlyIn(natasha, olga).
/* 'yes' if olga is inside katarina */
directlyIn(olga, katarina).

/* Base case */
contains(Doll1, Doll2) :- directlyIn(Doll2, Doll1).

/* Recursive case */
/* X becomes what ever the doll's pair is in the directlyIn() */
contains(Doll1, Doll2) :- directlyIn(X, Doll1), contains(X, Doll2).

test_answer :-
    findall(P, contains(P, irina), Output),
    sort(Output, SortedOutput),
    foreach(member(X,SortedOutput), (write(X), nl)).
