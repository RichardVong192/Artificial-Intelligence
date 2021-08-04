/*Base case */
mirror(leaf(Label), leaf(Label)).
/*Recursive case */
mirror(tree(B1, B2), tree(B3, B4)) :- mirror(B1, B4), mirror(B2, B3).

test_answer :-
    mirror(leaf(foo), leaf(foo)),
    write('OK'),
    halt.

test_answer :-
    write('Wrong answer!'),
    halt.
