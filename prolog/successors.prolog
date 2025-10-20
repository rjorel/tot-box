 
% Numbers defined as successor of 0.
num(0).
num(succ(X)) :- num(X).

add(0, Y, Y).
add(succ(X), Y, succ(Z)) :- add(X, Y, Z).
