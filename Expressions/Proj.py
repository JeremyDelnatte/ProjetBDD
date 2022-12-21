from copy import deepcopy
from Expressions.Expr import Expr
from Expressions.Rel import Rel
from Expressions.InvalidExpression import attributNotInSchemaError

class Proj(Expr):

    def __init__(self, attrs: list[str], expr: Expr):
        super().__init__()
        
        if (not isinstance(attrs, list) or not all(isinstance(attr, str) for attr in attrs)):
            raise TypeError("The type of attrs must be list[str].")
        
        elif (not isinstance(expr, Expr)):
            raise TypeError(f"The type of expr must be Expr, but is {type(expr).__name__}.")
        
        self.attrs = attrs
        self.expr = expr

    def __str__(self) -> str:
        return f"Proj({self.attrs}, {str(self.expr)})"

    def verify(self, db: str):
        
        self.expr.verify(db)
        attributes = self.expr.findAttributes(db)

        for attr in self.attrs:
            if (attr not in attributes):
                attributNotInSchemaError(self, attr, self.expr, attributes)

    def findAttributes(self, db: str) -> dict:
        
        attributes = self.expr.findAttributes(db)

        # On garde que les attributs qui sont dans attrs
        self.attributes = {}
        for attr in attributes:
            if (attr in self.attrs):
                self.attributes[attr] = attributes[attr]

        return self.attributes
    
    def toSQL(self, db: str) -> str:
        
        expr_SQL = self.expr.toSQL(db)

        # Une expression Rel est sous forme "select * from relName",
        # donc il est plus intéressant de mettre directement relName. 
        if (isinstance(self.expr, Rel)):
            expr_SQL = self.expr.relName

        # Pour les autres type d'expressions, on ne peut pas être sûr de la forme, donc on rajoute des ().
        else:
            expr_SQL = f"({expr_SQL})"

        return f"select distinct {', '.join(self.attrs)} from {expr_SQL}"