
% Grid check.
word(astante, a,s,t,a,n,t,e).
word(astoria, a,s,t,o,r,i,a).
word(baratto, b,a,r,a,t,t,o).
word(cobalto, c,o,b,a,l,t,o).
word(pistola, p,i,s,t,o,l,a).
word(stadale, s,t,a,d,a,l,e).

crossword(W1, W2, W3, W4, W5, W6) :-
    word(W1, _,A,_,B,_,C,_),
    word(W2, _,D,_,E,_,F,_),
    word(W3, _,G,_,H,_,I,_),
    word(W4, _,A,_,D,_,G,_),
    word(W5, _,B,_,E,_,H,_),
    word(W6, _,C,_,F,_,i,_).

% Very simple sentence builder.
word(article, un).
word(article, le).
word(verb, manger).
word(verb, lire).
word(noun, lion).
word(noun, lapin).

sentence(A1, N1, V, A2, N2) :-
    word(article, A1),
    word(noun, N1),
    word(verb, V),
    word(article, A2),
    word(noun, N2).

