
% a list and b list.
a2b([], []).
a2b([a | Ta], [b | Tb]) :- a2b(Ta, Tb).

% German number translation.
tran(eins, one).
tran(zwei, two).
tran(drei, three).
tran(vier, four).
tran(fuenf, five).
tran(sechs, six).
tran(sieben, seven).
tran(acht, eight).
tran(neun, nine).
tran(zehn, ten).

tranDeutschList([], []).
tranDeutschList([D | TD], [E | TE]) :-
    tran(D, E),
    tranDeutschList(TD, TE).

% Combinations.
combine1([], [], []).
combine1([X | TX], [Y | TY], [X, Y | TZ]) :-
    combine1(TX, TY, TZ).

combine2([], [], []).
combine2([X | TX], [Y | TY], [[X, Y] | TZ]) :-
    combine2(TX, TY, TZ).

combine3([], [], []).
combine3([X | TX], [Y | TY], [j(X, Y) | TZ]) :-
    combine3(TX, TY, TZ).

% Use case.
% combine([belle, damour, yeux, me], [marquise, vos, rougir, font], X).
