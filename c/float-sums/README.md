# Float sums

Que diriez-vous si je vous disais que le fait que votre calculatrice calcule `0.1 + 0.2` correctement
n'est pas trivial ? Et pourtant, c'est bien le cas..

En effet, vous n'êtes pas sans savoir que l'ensemble des nombres réels est un ensemble infini et indénombrable (qui
ne peut être mis en bijection avec l'ensemble des nombres relatifs, selon sa définition exacte, mais là je la cale
juste pour me la péter). Or nos pauvres ordinateurs sont incapables d'avoir de la mémoire infinie, donc il faut bien
limiter la représentation des nombres "à virgules". Ils se nomment "nombres flottants" en informatique. Et
`0.1` n'est
pas représentable précisément dans l'ensemble des flottants, du fait de la norme choisie pour les représenter, et
surtout du fait que l'ordinateur marche en binaire. Il y a de savants algorithmes pour sommer deux nombres flottants
de façon précise, et c'est grâce à cela que votre calculatrice vous répond bien `0.3`, car ces
algorithmes permettent justement d'avoir les résultats que l'on attend avec les données que nous entrons, qui sont
non-représentables en machine.

La norme la plus utilisée pour les représenter en machine est la norme IEEE-754, qui définit le format de
représentation, les valeurs spéciales, les opérations de bases (addition, soustraction, ..).

Malheureusement, malgré cette norme, les erreurs de calcul apparaîssent dès lors que l'on enchaîne les sommes de
nombres, à cause de l'accumulation d'erreurs minimes. Il existe des algorithmes de sommation exacte pour rémédier à
ces problèmes, qui calculent les erreurs et corrigent le résultat en fonction.

J'ai dû faire une petite étude de 12 algorithmes de sommation lors de ma 3° année de licence. 12 algorithmes
bidons, aucun d'eux ne donnant des résultats exacts, avec des ordres différents de sommation. Le
rapport explique plus en détails ces algorithmes.

`CMake` et `Gnuplot` sont requis pour faire fonctionner le script `run.sh`.
