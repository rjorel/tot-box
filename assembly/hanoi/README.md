# Hanoi

Le problème des tours de Hanoi est bien connu dans le monde de l'informatique. Il illustre bien l'utilité de la
récursivité dans certains cas.

Je laisse Wikipédia expliquer l'énoncé du problème :
[https://fr.wikipedia.org/wiki/Tours_de_Hano%C3%AF](https://fr.wikipedia.org/wiki/Tours_de_Hano%C3%AF)

Ce problème n'étant pas évident, un programme peut largement aider un humain. Seulement, comme tout est plus dur en
assembleur, ce programme propose une solution qui n'affiche que les déplacements pour 4 disques. Vous pouvez changer
la valeur de `%edi`, le registre qui représente le nombre de disques.

À l'affichage :
* _n_ : nombre de disques sur lequel on travaille.
* _d_ : tour de départ pour le déplacement d'un disque (le plus haut de la tour).
* _a_ : tour d'arrivée pour le déplacement.
