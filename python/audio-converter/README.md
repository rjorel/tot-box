# Audio converter

Cette petite appli web qui m'a permis de réfléchir à "comment créer un service en ligne à partir d'une commande
Linux". Étant donné que ce système d'exploitation n'est pas le plus utilisé et que le _shell_ reste encore
assez inaccessible aux personnes qui se déclarent elles-mêmes "nulles en informatique", proposer des services basés
sur Linux est toujours un peu compliqué.

Dans le cas présent, je cherchais à permettre l'utilisation de [FFMPEG](https://www.ffmpeg.org/) pour
convertir des fichiers audios. Bien que pléthore de sites le fassent déjà, mon cas d'usage était très particulier et
je devais m'assurer que les fichiers produits étaient exactement les mêmes (format + _codec_) que ceux que je
pouvais obtenir depuis mon ordinateur (sous Linux, évidemment !).

Le code est très simple et facilement adaptable à d'autres commandes (enfin je crois 😁). L'appli est basée sur
[Flask](https://flask.palletsprojects.com/) et utilise
[uWSGI](https://uwsgi-docs.readthedocs.io/) pour être servie dans une image
[Docker](https://www.docker.com/).
