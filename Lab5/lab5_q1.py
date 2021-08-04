/*If a variable is unused on prolog, we use an underscore.*/
/* Slice off the first and second element in the list. Then check if the second element sliced off
  matches the second element in the predicate */
second([_, Head2|_], Head2).

test_answer :-
    \+ second([1], X),
    writeln('OK').

test_answer :-
    second([_],_),
    writeln('The predicate should fail on lists of length one!').
