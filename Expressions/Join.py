from copy import deepcopy
from Expressions.Expr import Expr
from Expressions.Rel import Rel

class Join(Expr):

    def __init__(self, expr1: Expr, expr2: Expr):
        super().__init__()
        
        if (not isinstance(expr1, Expr)):
            raise TypeError(f"The type of expr1 must be Expr, but is {type(expr1).__name__}.")
        
        elif (not isinstance(expr2, Expr)):
            raise TypeError(f"The type of expr2 must be Expr, but is {type(expr2).__name__}.")

        self.expr1 = expr1
        self.expr2 = expr2
        self.intersectAttributes = []

    def __str__(self) -> str:
        return f"Join({str(self.expr1)}, {str(self.expr2)})"
    
    def findAttributes(self, db: str) -> list:

        if (db != self.db):
            self.db = db

            self.attributes = deepcopy(self.expr1.findAttributes(db))
            attributes2 = self.expr2.findAttributes(db)

            for attr in attributes2:
                if (attr not in self.attributes):
                    self.attributes.append(deepcopy(attr))

                else:
                    self.intersectAttributes.append(deepcopy(attr))

        return self.attributes

    def toSQL(self, db: str) -> str:
        expr1_SQL = self.expr1.toSQL(db)
        expr2_SQL = self.expr2.toSQL(db)

        self.findAttributes(db)

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

        # Si les deux listes ont le même nombre d'attributs, ça siginifie donc qu'elles ont les mêmes attributs.
        # Et donc on fait l'intersection entre les deux tables.
        if (len(self.intersectAttributes) == len(self.attributes)):
            return f"select * from {expr1_SQL} intersect select * from {expr2_SQL}"
        
        # Dans les autres cas, on fait un natural join. (Un natural join fonctionnerait aussi au dessus mais ne retire pas les doublons(à part si on met distinct))
        else:
            return f"select * from {expr1_SQL} natural join {expr2_SQL}"