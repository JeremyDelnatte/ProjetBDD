# Rapport de projet de *Bases de Données 1*
# Compilation __SPJRUD__ vers __SQL__

## Introduction

L'objectif de ce projet est d'implémenter, en _Python_, un outil de traduction de requêtes __SPJRUD__ vers des requêtes __SQL__. Cet outil doit permettre de traduire des requêtes __SPJRUD__ vers l'expression d'une requête __SQL__, doit pouvoir vérifier que l'expression __SPJRUD__ est correcte et doit permettre d'executé facilement ces requêtes sur une base de données __SQLite__.

## Choix d'implémentation

Il existe sans doute plusieurs façon de faire ce projet, mais nous avons décider de le faire orienté objet. On a créer un classe _Expr_ qui est une classe abstraite, qui est un classe parent de tous les opérateurs __SPJRUD__. Elle nous permet d'appeler les méthodes _findAttributes()_, _verify()_ et _toSQL()_ sur les opérateurs. 
La méthode _findAttributes()_ permet de récupérer les attributs de la sous expression et de calculer en suivant de l'opérateur les nouveaux attributs de l'expression, si la sous expression est une relation, on récupére les attributs depuis le schema de la table dans la base de données __SQLite__.
Nous avons décidé d'utiliser un dictionnaire pour stocker les attributs d'une expression avec comme clé le nom de l'attribut et comme valeur le type de l'attributs, en python le dictionnaire garde l'orde d'insertion des clés, donc pas besoin d'avoir une liste pour garder le bonne ordre.
Nous avons décidé que la méthode _findAttributes()_ devais être appelé avant les méthodes _verify()_ et _toSQL()_, pour éviter beaucoup d'appels redondants. De même avec la méthode _verify()_ doit être appelé avec la méthode _toSQL()_. Pour ce faire nous avons décidé que ces méthodes n'allaient pas directement être utiliser par les utilisateurs, mais ils vont plutôt utiliser les méthodes _toSQL()_ et _verify()_ de _Execution.py_, qui vont appelé pour les utilisateurs les méthodes citées au dessus.

## Difficulté

Au cours de l'implémentation, la seul majeur difficulté que nous avons rencontrés, c'était de comprendre comment traduire des requêtes __SPJRUD__ vers des requêtes __SQL__.

## Fonctionnalités supplémentaires



## Utilisation





## Conclusion

