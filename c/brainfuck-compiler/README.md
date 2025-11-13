# Brainfuck compiler

Ceci est un compilateur source-to-source. Il transforme un programme écrit en Brainfuck vers du C, cela étant tout
de même relativement simple.

Pour faire court, le Brainfuck est un langage Turing-complet (on peut normalement tout faire avec y compris des
interfaces graphiques) comprenant 8 instructions. Nous disposons d'un tableau de 30000 cases initialisées à 0, et le
programme débute à la première case (indice 0).

**Instructions :**

* `+` : incrémente la case courante,
* `-` : décrémente la case courante,
* `<` : revient une case en arrière,
* `>` : avance d'une case,
* `[` : exécute la suite d'instruction si la case courante est différente de 0, et ce jusqu'au prochain `]`,
* `]` : expliqué juste au-dessus,
* `,` : demande un caractère à l'utilisateur et le stocke dans la case courante,
* `.` : affiche le caractère correspondant à la case courante.

Tous les autres caractères sont considérés comme des commentaires.

Un exemple tiré de Wikipedia est fourni, avec les explications pour comprendre comment cela fonctionne.
