# Rapport de projet de *Bases de Données 1*
# Compilation __SPJRUD__ vers __SQL__

## Auteurs

-   Jérémy Delnatte
-   Tonesko Djoufo Tafejo

## Introduction

L'objectif de ce projet est d'implémenter, en _Python_, un outil de traduction de requêtes __SPJRUD__ vers des requêtes __SQL__. Cet outil doit permettre de traduire des requêtes __SPJRUD__ vers l'expression d'une requête __SQL__, doit pouvoir vérifier que l'expression __SPJRUD__ est correcte et doit permettre d'executé facilement ces requêtes sur une base de données __SQLite__.

## Choix d'implémentation

Il existe sans doute plusieurs façon de faire ce projet, mais nous avons décider de le faire orienté objet. On a créer un classe `Expr` qui est une classe abstraite, qui est un classe parent de tous les opérateurs __SPJRUD__. Elle nous permet d'appeler les méthodes`findAttributes()`, `verify()` et `toSQL()` sur les opérateurs. 
La méthode `findAttributes()` permet de récupérer les attributs de la sous expression et de calculer en suivant de l'opérateur les nouveaux attributs de l'expression, si la sous expression est une relation, on récupére les attributs depuis le schema de la table dans la base de données __SQLite__.
Nous avons décidé d'utiliser un dictionnaire pour stocker les attributs d'une expression avec comme clé le nom de l'attribut et comme valeur le type de l'attributs, en python le dictionnaire garde l'orde d'insertion des clés, donc pas besoin d'avoir une liste pour garder le bonne ordre.
Nous avons décidé que la méthode `findAttributes()` devais être appelé avant les méthodes `verify()` et `toSQL()`, pour éviter beaucoup d'appels redondants. De même avec la méthode `verify()` doit être appelé avec la méthode `toSQL()`. Pour ce faire nous avons décidé que ces méthodes n'allaient pas directement être utiliser par les utilisateurs, mais ils vont plutôt utiliser les méthodes `toSQL()` et `verify()` de _Execution.py_, qui vont appelé pour les utilisateurs les méthodes citées au dessus.

## Difficulté

Au cours de l'implémentation, la seul majeur difficulté que nous avons rencontrés, c'était de comprendre comment traduire des requêtes __SPJRUD__ vers des requêtes __SQL__.

## Fonctionnalités supplémentaires

Nous avons décider d'ajouter les fonctionnalités supplémentaires proposer dans l'énoncé du projet. À savoir:
-   Convertir une expression __SPJRUD__ en une chaîne de caractères, pour ce faire nous avons redéfini la méthode `__str__()` de chaque opération.
-   `createTableFromQuery()` qui permet créer une nouvelle table à partir d'une requête __SQL__.
-   `printResultFromQuery()` qui permet d'afficher le résultat d'une requête dans le terminal. 

## Utilisation

Pour créer un requête en __SPJRUD__, il faut utiliser les objets de type `Expr`, c'est-à-dire tous les opérateurs suivants: 
-   `Rel(relName)` où _relName_ est le nom de la relation;
-   `Select(attr1, operator, attr2, expr)` où _attr1_ est l'attribut à gauche de l'opérateur, _operator_ est l'opérateur, _attr2_ est soit une constante _Cst_ ou soit un attribut à droite de l'opérateur et _expr_ est la sous expression;
    -   `Cst(cst)` où _cst_ est une constante;
-   `Diff(expr1, expr2)` où _expr1_ et _expr2_ sont les sous expressions. 
-   `Proj(attrs, expr)` où _attrs_ est la liste des attributs projeter et _expr_ est la sous expression;
-   `Join(expr1, expr2)` où _expr1_ et _expr2_ sont les sous expressions. 
-   `Rename(attr, name, expr)` où _attr_ est l'attribut qui va être renommer, _name_ est le nom qui va être donné à l'attribut et _expr_ est la sous expression;
-   `Union(expr1, expr2)` où _expr1_ et _expr2_ sont les sous expressions. 

Pour pouvoir traduire une requête __SPJRUD__ en une requête __SQL__, il faut utiliser la méthode `toSQL(expr, db)` de _Execution.py_ où _expr_ est l'expression en __SPJRUD__ et _db_ est le nom de la base de données __SQLite__ utilisé. Et pour vérifier une requête __SPJRUD__, il faut utiliser la méthode `verify(expr, db)` de _Execution.py_.

Il est aussi possible d'exécuter une requête __SPJRUD__ avec la méthode `executeRequest(expr, db)`, la méthode va traduire pour nous la requête en __SQL__ puis va l'executer avec __SQLite__.

Pour créer une nouvelle table à partir d'une requête __SQL__ avec la méthode `createTableFromQuery(query, tableName, db)` où _query_ est la requête __SQL__, _tableName_ est le nom de la nouvelle table et _db_ est le nom de la base de données __SQLite__. Il est aussi possible afficher le résultat d'une requête __SQL__ avec la méthode `printResultFromQuery(query, db)`.