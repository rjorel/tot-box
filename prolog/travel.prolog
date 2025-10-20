
% Travel itinerary.
inCar(auckland, hamilton).
inCar(hamilton, raglan).
inCar(valmont, sarrebruck).
inCar(valmont, metz).

inTrain(metz, francfort).
inTrain(sarrebruck, francfort).
inTrain(metz, paris).
inTrain(sarrebruck, paris).

inPlane(francfort, bangkok).
inPlane(francfort, singapour).
inPlane(paris, losAngeles).
inPlane(bangkok, auckland).
inPlane(singapour, auckland).
inPlane(losAngeles, auckland).

travel(X, Y) :- 
    inCar(X, Y);
    inTrain(X, Y);
    inPlane(X, Y).

travel(X, Y) :-
    inCar(X, Z),
    travel(Z, Y);
    
    inTrain(X, Z),
    travel(Z, Y);
    
    inPlane(X, Z),
    travel(Z, Y).

% Tranport means are saved.
travel(X, Y, car(X, Y)) :- inCar(X, Y).
travel(X, Y, train(X, Y)) :- inTrain(X, Y).
travel(X, Y, plane(X, Y)) :- inPlane(X, Y).

travel(X, Y, car(X, Z, W)) :- 
    inCar(X, Z),
    travel(Z, Y, W).

travel(X, Y, train(X, Z, W)) :- 
    inTrain(X, Z),
    travel(Z, Y, W).
 
travel(X, Y, plane(X, Z, W)) :- 
    inPlane(X, Z),
    travel(Z, Y, W).
