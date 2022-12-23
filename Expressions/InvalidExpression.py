from Expressions.Expr import Expr

def schemaNotEqualError(expr: Expr, subExpr1: Expr, subExpr2: Expr, attrs1: dict, attrs2: dict):
    """
    Permet d'afficher l'erreur lorsque les schémas des sous expressions ne sont pas égaux.

            Parameters:
                    expr (Expr): L'expression où a eu lieu l'erreur
                    subExpr1 (Expr): La sous expression 1 de expr
                    subExpr2 (Expr): La sous expression 2 de expr
                    attrs1 (dict): Le dictionnaire des attributs de la sous expression 1
                    attrs2 (dict): Le dictionnaire des attributs de la sous expression 2

            Returns:
                    None
    """

    print("Invalid expression.", "The (sub-)expression", "  " + str(expr), "is invalid because the schema of", "  " + str(subExpr1), "which is", sep="\n")
    printSchema(attrs1)
    print("is not the same as the one from", "  " + str(subExpr2), "which is", sep="\n")
    printSchema(attrs2)

    exit()

def attributNotInSchemaError(expr: Expr, attr: str, subExpr: Expr, attrs: dict):
    """
    Permet d'afficher l'erreur lorsqu'un attribut n'est pas dans le schéma de la sous expression.

            Parameters:
                    expr (Expr): L'expression où a eu lieu l'erreur
                    subExpr (Expr): La sous expression de expr
                    attrs (dict): Le dictionnaire des attributs de la sous expression

            Returns:
                    None
    """

    print("Invalid expression.", "The (sub-)expression", "  " + str(expr), "is invalid because the attribute", "  " + attr, "is not in the schema of", "  " + str(subExpr), "which is", sep="\n")
    printSchema(attrs)

    exit()

def sameAttributsDifferentTypeError(expr: Expr, attr: str, subExpr1: Expr, subExpr2: Expr, attrs1: dict, attrs2: dict):
    """
    Permet d'afficher l'erreur lorsque deux attributs avec le même nom dans les deux sous expressions ont un type différent.

            Parameters:
                    expr (Expr): L'expression où a eu lieu l'erreur
                    attr (str): L'attribut qui a un type différent dans les deux schéma
                    subExpr1 (Expr): La sous expression 1 de expr
                    subExpr2 (Expr): La sous expression 2 de expr
                    attrs1 (dict): Le dictionnaire des attributs de la sous expression 1
                    attrs2 (dict): Le dictionnaire des attributs de la sous expression 2

            Returns:
                    None
    """

    print("Invalid expression.", "The (sub-)expression", "  " + str(expr), "is invalid because the attribute", "  " + attr, sep="\n")
    print("is not the same in the schema of", "  " + str(subExpr1), "which is", sep="\n")
    printSchema(attrs1)
    print("as in the schema of", "  " + str(subExpr2), "which is", sep="\n")
    printSchema(attrs2)
    
    exit()

def differentTypeError(expr: Expr, attr1: str, attr2: str, subExpr: Expr, attrs: dict):
    """
    Permet d'afficher l'erreur lorsque deux attributs ont un type différent dans le même schéma.

            Parameters:
                    expr (Expr): L'expression où a eu lieu l'erreur
                    attr1 (str): L'attribut 1
                    attr2 (str): L'attribut 2
                    subExpr (Expr): La sous expression de expr
                    attrs (dict): Le dictionnaire des attributs de la sous expression

            Returns:
                    None
    """

    print("Invalid expression.", "The (sub-)expression", "  " + str(expr), "is invalid because the attributes", "  " + attr1 + " and " + attr2, sep="\n")
    print("don't have the same type in the schema of", "  " + str(subExpr), "which is", sep="\n")
    printSchema(attrs)

    exit()

def tableDoesNotExistsError(expr: Expr, relName: str):
    """
    Permet d'afficher l'erreur lorsque une table n'existe pas dans la base de données.

            Parameters:
                    expr (Expr): L'expression où a eu lieu l'erreur
                    relName (str): Le nom de la table qui n'existe pas 

            Returns:
                    None
    """

    print("Invalid expression.", "The (sub-)expression", "  " + str(expr), "is invalid because the table", "  " + relName, "does not exists in the db.", sep="\n")
    
    exit()

def attributAlreadyExists(expr: Expr, name: str, subExpr: Expr, attrs: dict):
    """
    Permet d'afficher l'erreur lorsque une table n'existe pas dans la base de données.

            Parameters:
                    expr (Expr): L'expression où a eu lieu l'erreur
                    name (str): Le nom qui existe déjà dans le schéma de la sous expression
                    subExpr (Expr): La sous expression de expr
                    attrs (dict): Le dictionnaire des attributs de la sous expression

            Returns:
                    None
    """

    print("Invalid expression.", "The (sub-)expression", "  " + str(expr), "is invalid because the attribute", "  " + name, sep="\n")
    print("already exists in the schema of", "  " + str(subExpr), "which is", sep="\n")
    printSchema(attrs)

    exit()

def printSchema(attrs: dict):
    """
    Permet d'afficher le schéma d'une expression.

            Parameters:
                    attrs (dict): Le dictionnaire des attributs d'une expression

            Returns:
                    None
    """

    for i, attr in enumerate(attrs):

        print(f"  '{attr}' {attrs[attr]}", end="")

        if (i != len(attrs) - 1):
            print(",")
        else:
            print()