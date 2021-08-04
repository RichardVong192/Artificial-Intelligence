/*Success when two lists are identical, except when the first two elements are exchanged*/
swap12([Head1, Head2|Tail], [Head2, Head1 | Tail]).

test_answer :-
    swap12([a, b, c, d], L),
    writeln(L).

test_answer2 :-
    \+ swap12(L, [1]),
    writeln('OK').

test_answer3 :-
    swap12(L, [b, a]),
    writeln(L).

test_answer4 :-
  swap12(L1, L2),
  writeln('OK').
