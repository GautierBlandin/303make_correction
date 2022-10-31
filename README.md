# Correction 303make

## Introduction
L'objectif de ce corrigé est de vous aider à aborder des sujets complexes en programmation appliquée aux Mathématiques.

## Projet

Le 303make consiste à créer un programme capable de générer puis d'analyser un graphe de dépendances à partir d'un fichier Makefile.

## Étapes

Lorsque vous abordez un projet de ce type, vous devez immédiatement vous poser plusieurs questions :
- Quelles sont les sous-problèmes à résoudre pour résoudre le problème global ?
- Quelles sont les structures de données à utiliser pour résoudre ces sous-problèmes ?

Ici, les sous-problèmes importants sont :
- Le parsing du Makefile, i.e. l'extraction des données texte et leur conversion dans un format utilisable
- La génération du graphe de dépendances à partir des données du Makefile
- L'analyse du graphe de dépendances pour déterminer les chemins possibles (partie 1) et les commandes à exécuter (partie 2)
- L'affichage de vos résultats dans la console

La structure de donnée principale à utiliser est un graphe orienté, et donc une matrice d'adjacence et/ou une liste d'adjacence.

<b>Évitez de foncer tête baissée dans le code avant d'avoir compris les étapes que vous allez devoir suivre.</b>

## Organisation du corrigé

Une fois que les différents sous-problèmes sont déterminés, vous pouvez vous attaquer au code. Séparer les étapes logiques en différents modules est utile pour avoir un code compréhensible, et vous pouvez aller plus loin en regroupant les modules liés dans des packages.

Le corrigé propose l'organisation suivante :
- graph_format_conversion.py, graph_search.py : Modules relatifs à la logique des graphes.
- parsing.py, dependency.py : Parsing du fichier en données utilisables, dependency.py définit une classe pour ça, on aurait aussi pu utiliser des dictionnaires python
- graph_generation.py : Génération du graphe de dépendance à partir des données récupérées. <b> C'est une étape séparée du parsing : Le parsing consiste uniquement à obtenir des données utilisables, la génération du graphe est un traitement à part </b>
- printing.py : Affichage des résultats obtenus
- 303make, part1.py, part2.py : Combinaisons des différents modules pour traiter le sujet

## Tests unitaires

Une fois que votre projet est bien séparé en différents sous-problèmes, il est en général assez facile de définir les fonctions dont vous avez besoin. Quand on code, on a souvent le bon réflexe de vérifier que la fonction qu'on vient de coder fait bien ce qu'on attend d'elle. Pour aller plus loin et systématiser ce processus, il est très simple d'écrire des tests unitaires qui vérifient qu'une fonction fait bien ce qu'on veut. En étant sûr que chaque partie de votre programme fait ce que vous attendez, c'est probable que mises ensemble, le tout se comporte comme vous le souhaitez.

En python, l'écriture de tests unitaires est intégrée au langage, mais la librairie pytest est recommandée pour simplifier leur développement.

Une organisation recommandée est de reproduire l'architecture de votre projet dans un dossier de test. Il suffit ensuite de lancer la commande pytest à la racine du projet pour que tous les tests soient exécutés.

## Conclusion

Pour vous simplifier la vie dans les projets qui arrivent, prenez le temps de réfléchir aux sous-problèmes de chaque projet et codez proprement. Vous prendrez (peut-être) un tout petit plus de temps avant d'avoir une première version de votre programme, mais elle aura beaucoup plus de chance de passer la majorité des tests et le debugging sera beaucoup plus simple pour les tests qui fail.

Les projets suivants ne seront pas moins complexes que le 303make, donc prenez les bonnes habitudes le plus vite possible.