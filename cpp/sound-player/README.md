# Sound player

Lors de ma dernière année de licence, nous avions à programmer un robot Mindstorm, qui permettait entre autres de
jouer des sons.

Comme le programme que je faisais avec mon binôme n'était pas des plus compliqués, je me suis dit qu'on pouvait
rajouter des petites musiques en fonctions des situations dans lesquelles se trouvait le robot, mais pour cela il
fallait préciser toutes les notes en donnant leur fréquence.. ce qui était assez fastidieux.

D'où l'idée de faire cela avec un programme, et comme à l'époque je ne connaissais pas les domaines de prédilection
de certains langages (notamment Python), j'ai écrit un programme simple qui lisait un fichier représentant les
cordes et les frets d'une guitare pour traduire cela en tableau de fréquences. Il est clair que Python aurait été
plus approprié dans ce cas.

Pour le coup, j'ai retapé le programme pour qu'il lise un fichier et le joue directement. Chaque note est formatée
de la manière suivante : `fret corde durée`. Deux fichiers sont donnés en exemples.

Afin de pouvoir compiler le programme, il est nécessaire d'installer les fichiers de développement de
`pulse audio`.
