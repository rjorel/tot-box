# Sudoku solver

Un grand classique en programmation pour apprendre une application de l'algorithme de "retour sur trace"
(_backtracking_).

Dans le cas de la résolution d'une grille de sudoku, il s'agit de progresser dans les cases de la grille et de
tester toutes les valeurs de 1 à 9 pour chaque case, en prenant en compte celles qui sont déjà remplies. Si aucune
valeur ne peut être attribuée à une case donnée, l'algorithme revient en arrière et tente de modifier les valeurs de
cases déjà affectées pour pouvoir de nouveau progresser par la suite.

C'est un algorithme qualifié de glouton, mais dans les faits il est quand même bien rapide pour la résolution d'une
grille de sudoku.
