/*Base case - define all possible trees*/
tree(_, leaf(_), leaf(_)).
tree(_, leaf(_), tree(_)).
tree(_, tree(_), leaf(_)).
tree(_, tree(_), tree(_)).
leaf(_).

/*Recursive case */
preorder(tree(Root, Left, Right), T) :-
      preorder(Left, LeftSubTree),
      preorder(Right, RightSubTree),
      append([Root|LeftSubTree], RightSubTree, T).

preorder(leaf(Root), [Root]).

test_answer :- preorder(leaf(a), Left),
               writeln(Left).

test_answer2 :- preorder(tree(a, tree(b, leaf(c), leaf(d)), leaf(e)), T),
              writeln(T).
