/*Base case - translation of empty list is empty list*/
listtran([], []).
/*Recursive case - true if head1 and head2 are equal in the knowledge base AND Tail1 and Tail2 are themselves a list translation*/
listtran([Head1|Tail1], [Head2|Tail2]) :- tran(Head1, Head2) , listtran(Tail1, Tail2).

tran(eins,one).
tran(zwei,two).
tran(drei,three).
tran(vier,four).
tran(fuenf,five).
tran(sechs,six).
tran(sieben,seven).
tran(acht,eight).
tran(neun,nine).


test_answer :-
    listtran([eins, neun, zwei], X),
    writeln(X).

test_answer2 :-
    listtran([], []),
    writeln('OK').

test_answer3 :-
    listtran(X, [one, seven, six, two]),
    writeln(X).

test_answer4 :-
    listtran(L1, L2),
    writeln('OK').
