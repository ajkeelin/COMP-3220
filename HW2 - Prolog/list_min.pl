minl([Only], Only).
minl([Head|Tail], Minimum) :-
	minl(Tail, TailMin),
	Minimum is min(Head, TailMin).

list_min(L, M) :-
    minl(L, X),
    (   X == M ->  true ; false).