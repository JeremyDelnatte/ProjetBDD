from Expressions.Expr import Expr
from sqlite3 import Cursor, connect

def toSQL(expr: Expr, db: str) -> str:
    """
    Permet de traduire une expression en SPJRUD en une requête SQL.

            Parameters:
                    expr (Expr): L'expression SPJRUD 
                    db (str): La base de données

            Returns:
                    str : La requête SQL
    """

    verify(expr, db)
    return expr.toSQL()

def verify(expr: Expr, db: str):
    """
    Permet de vérifier si une expression en SPJRUD est correcte.

            Parameters:
                    expr (Expr): L'expression SPJRUD 
                    db (str): La base de données

            Returns:
                    None
    """

    expr.findAttributes(db)
    expr.verify()

def executeRequest(expr: Expr, db: str) -> list:
    """
    Permet de directement exécuter un requête SPJRUD. La méthode traduis la requête SPJRUD en SQL pour nous.

            Parameters:
                    expr (Expr): L'expression SPJRUD 
                    db (str): La base de données 

            Returns:
                    list : Le résultat de la requête
    """
    cur = connect(db).cursor()
    return cur.execute(toSQL(expr, db)).fetchall()
