/*Base case - When an empty list equals an empty list */
remove(_, [], []).

/*Recursive case */
/*Case 1 - When the head of the list is the thing you want to remove */
/*Case 2 - When the head of the list is not the head of the list, so you you remove the head from list1 and add it to list2 */
remove(X, [X|Tail1], Tail2) :- remove(X, Tail1, Tail2).
remove(X, [Head|Tail1], [Head|Tail2]) :- remove(X, Tail1, Tail2).

test_answer :-
    remove(a, [a, b, a, c, d, a, b], L),
    writeln(L).

test_answer2 :-
    remove(2, [2], L),
    writeln(L).

test_answer3 :-
    remove(d, [a, b, c], L),
    write(L).

test_answer4 :-
    remove(a, [], L),
    write(L).

test_answer5 :-
    remove(term2, [term1, term2, term3], [term1, term3]),
    write('OK').
