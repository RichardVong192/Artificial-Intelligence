/*Base case - when it is an empty list*/
/*Recursive case - odd calls even and even calls odd until it is at base case */
even([], [], []).
even([Head|Tail], OddIndexList, [Head|EvenIndexList]) :- odd(Tail, OddIndexList, EvenIndexList).

odd([], [], []).
odd([Head|Tail], [Head|OddIndexList], EvenIndexList) :- even(Tail, OddIndexList, EvenIndexList).

split_odd_even(L, OddIndexList, EvenIndexList) :- odd(L, OddIndexList, EvenIndexList).

test_answer :-
    split_odd_even([a,b,c,d,e,f,g], A, B),
    write(A),
    writeln(B).


test_answer2 :-
    split_odd_even([1,2,3,5], A, B),
    write(A),
    writeln(B).
