
% Connections between points.
connection(1, 2).
connection(3, 4).
connection(5, 6).
connection(7, 8).
connection(9, 10).
connection(12, 13).
connection(13, 14).
connection(15, 16).
connection(17, 18).
connection(19, 20).
connection(4, 1).
connection(6, 3).
connection(4, 7).
connection(6, 11).
connection(14, 9).
connection(11, 15).
connection(16, 12).
connection(14, 17).
connection(16, 19).

path(X, Y) :- connection(X, Y).
path(X, Y) :-
    connection(X, Z),
    path(Z, Y).
