
% Genealogic tree.
is_son(raph, manu).
is_son(truc, raph).

is_descendant(X, Y) :- is_son(X, Y).
is_descendant(X, Y) :-
    is_son(X, Z),
    is_descendant(Z, Y).
