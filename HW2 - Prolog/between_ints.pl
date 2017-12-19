between_ints(I, J, K) :-
    (   I =< K ->  true ; false),
    (   K =< J ->  true ; false);
    
    (   I >= K ->  true ; false),
    (   K >= J ->  true ; false).