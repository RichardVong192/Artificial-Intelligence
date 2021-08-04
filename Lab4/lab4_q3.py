reflection(point(X, Y), point(Y, X)).
/* reflection is a rule and the rule state that it is 'yes' if and only if point(x, y) == point(y,x) */

test_answer :-
	reflection(point(-5, 8), point(X, Y)),
        writeln(point(X, Y)).
