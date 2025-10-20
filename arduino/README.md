#  Arduino

J'ai très peu touché à Arduino, bien que je m'en sois procuré un il y a quelques années. J'ai voulu m'y initier mais
n'ayant pas de réel but ni d'idées particulières à réaliser, je n'ai pas réussi à poursuivre sérieusement
l'apprentissage de cette technologie.

Cependant, une fois où un ami devait s'en servir et m'en avait fait part pour savoir si je pouvais l'aider,
j'ai cherché à me passer de l'IDE développé par l'équipe d'Arduino.. parce que, soyons honnête, cet IDE est moisi.
Mais VRAIMENT moisi. Seul petit problème : l'IDE permet de téléverser (oui, je me sers de ce mot à la place de
l'anglissisme _uploader_) un programme sur les cartes Arduino très simplement, ce qui s'avère bien moins aisé
si l'on cherche à le faire "à la main".

Fort heureusement, des gens sympas ont développé un module `make` nommé `android-mk` qui
permet de compiler ET téléverser un programme.. la belle vie quoi. Enfin, sous Linux au moins, parce que sous
Windows, je ne sais pas du tout si ça marche.

Voici donc un cas d'utilisation de ce module, j'ai développé une surcouche très simple d'EEPROM pour l'exemple. Le
fichier `Android.mk` permet de configurer le programme en fonction de votre carte Arduino, et le
script `deploy.sh` montre comment téléverser le code et également lancer un moniteur pour écouter les
sorties de la carte Arduino. Ce moniteur fait partie du _package_ Python `pyserial` et le port qu'il
écoute dans le script pourrait être différent sur votre machine (il doit correspondre logiquement à la valeur
`MONITOR_PORT` du fichier `Android.mk`).
