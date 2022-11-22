from copy import deepcopy
from Expressions.Expr import Expr
from Expressions.Rel import Rel

class Diff(Expr):

    def __init__(self, expr1: Expr, expr2: Expr):
        
        if (not isinstance(expr1, Expr)):
            raise TypeError(f"The type of expr1 must be Expr, but is {type(expr1).__name__}.")
        
        elif (not isinstance(expr2, Expr)):
            raise TypeError(f"The type of expr2 must be Expr, but is {type(expr2).__name__}.")

        self.expr1 = expr1
        self.expr2 = expr2

    def __str__(self) -> str:
        return f"Diff({str(self.expr1)}, {str(self.expr2)})"
    
    def findAttributes(self, db: str) -> list:
        
        if (db != self.db):
            self.db = db
            self.attributes = deepcopy(self.expr1.findAttributes(db))

        return self.attributes

    def toSQL(self, db: str) -> str:
        expr1_SQL = self.expr1.toSQL(db)
        expr2_SQL = self.expr2.toSQL(db)

        # Une expression Rel est sous forme "select * from relName",
        # donc il est plus intéressant de mettre directement relName. 
        if (isinstance(self.expr1, Rel)):
            expr1_SQL = self.expr1.relName

        # Pour les autres type d'expressions, on ne peut pas être sûr de la forme, donc on rajoute des ().
        else:
            expr1_SQL = f"({expr1_SQL})"

        # (Voir au dessus)
        if (isinstance(self.expr2, Rel)):
            expr2_SQL = self.expr2.relName

        else:
            expr2_SQL = f"({expr2_SQL})"

        return f"select * from {expr1_SQL} except select * from {expr2_SQL}"
        