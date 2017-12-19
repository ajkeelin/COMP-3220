p(X) :-
    append(L, R, X),
    length(L, A),
    length(R, B),
    (   A \== B ->  false ; true),
    (   member('b', L) ->  false ; true),
    (   member('a', R) ->  false ; true).