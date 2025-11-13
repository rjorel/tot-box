# Huffman compression

En 2ème année de licence, j'ai eu comme projet de réaliser l'algorithme de compression de Huffman.

L'idée de celui-ci est de représenter les caractères qui apparaissent le plus souvent par des codes prenant moins
de place en mémoire. Il faut pour cela construire un arbre permettant de déduire facilement les encodages de chaque
caractère.

L'algorithme marche bien sur les fichiers sans compression, notamment les fichiers texte. En revanche, il ne fait
pas gagner grand-chose sur les images ou les vidéos, car ces fichiers sont souvent déjà compressés et utilisent des
algorithmes propres à leurs domaines.

Je l'ai ré-écrit en grande partie par la suite, pour le rendre plus facilement plus lisible. Cependant, en faisant
cela et dans le but de ne pas alourdir le code, la gestion de la fin de fichier n'est pas parfaite. De ce fait, il
se peut que certains caractères soient rajoutés à la fin d'un fichier (surtout visible avec les fichiers textes, les
images ou les vidéos ne semblent pas être autant affectées).
