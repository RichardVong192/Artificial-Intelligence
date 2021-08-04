/*bob eats chocolate if bob likes chocolate */
eats(X,Y) :- likes(X,Y).

/*bob eats if he is hungry and desparate and food is edible */
eats(X,C):- edible(C), hungry(X).


likes(bob, chocolate).
hungry(alice).

test_answer :- eats(bob, chocolate),
               writeln('Bob eats chocolate.').
