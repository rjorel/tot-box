# cMind

Ceci est un projet résultant de mon premier stage de recherche en 3ème année de licence.

En réalité, je ne pense pas que mon travail puisse être utile à quelqu'un, à moins de tomber sur une personne qui
cherche à comprendre cet outil (s'il existe encore).

Ce fut une vraie galère de savoir comment se servir de cet outil d'_auto-tuning_, censé optimiser de façon
automatique un programme C. Ce qu'il fait peut être assez facilement résumé : il applique des séries aléatoires
d'optimisations pour un compilateur pré-configuré et fait des mesures de performances.

A la fin du stage, je me suis rendu compte que l'optimisation la plus puissante de GCC (à savoir `-O3`)
donnait toujours les meilleures performances.. cela dit, je me demande si mes conclusions étaient bonnes, car je ne
pense pas que cette optimisation permettait d'avoir des résultats justes sur les algorithmes de sommation que je
devais traiter.
