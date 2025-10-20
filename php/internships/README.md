# Internships

Dans le top des sujets de projets bien originaux, je vous présente celui-ci. Je l'ai fait en Licence 3 avec
[Stanislas Pagès](https://www.linkedin.com/in/stanislas-pag%C3%A8s-1285aa150/), et il
consiste à gérer des stages proposés par des entreprises.. quand je vous parlais d'originalité.

Ceci dit, l'idée était de gérer plusieurs types d'utilisateurs avec différents privilèges, et le travail n'a pas été
simple. L'accent était vraiment mis sur la conception de la base de données, mais le développement du site a été
assez chronophage. Le prof ne voulait aucun style, donc le site est assez moche, néanmoins - au vu de la
non-originalité du sujet - peut-être que quelques idées pourront être reprises.

Le style du rapport est un peu enfantin par endroit, mais je l'ai mis tel que je l'avais fait avec mon binôme. Au
niveau du code, j'ai juste clarifié le style (parce que je codais de manière très compacte à l'époque), et débuggé
quelques trucs.

Comme c'est une peu bordélique tout de même, n'hésitez pas à me poser des questions via le formulaire de contact,
pour tout problème de compréhension. Pour simplifier la prise en main du projet, j'ai ajouté de quoi l'exécuter
avec _Docker_ et _Docker Compose_. Une fois la commande `docker-compose up` lancée, le site
sera disponible à l'adresse [http://localhost:8000/](http://localhost:8000/). Pour initialiser la base de
donnée, il faudra taper la commande
`docker-compose exec -T database mysql -u root -psecret homestead < database.sql`. Le compte admin a les
les identifiants `admin / admin` (très original, vous en conviendrez).
