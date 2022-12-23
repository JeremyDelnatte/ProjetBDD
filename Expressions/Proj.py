from copy import deepcopy
from Expressions.Expr import Expr
from Expressions.Rel import Rel
from Expressions.InvalidExpression import attributNotInSchemaError

class Proj(Expr):
    """
    Classe qui représente l'opérateur Project en SPJRUD.

            Attributes:
                    attributes (dict): Le dictionnaire des attributs avec comme clé le nom et comme valeur le type de l'attribut
                    attrs (list[str]): La liste des attributs à projeter.
                    expr (Expr): La sous expression
    """

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

    def verify(self):
        
        self.expr.verify()
        attributes = self.expr.attributes

        # Permet de vérifier si les attributs à projeter sont dans les attributs de expr.
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
    
    def toSQL(self) -> str:
        
        expr_SQL = self.expr.toSQL()

        # Une expression Rel est sous forme "select * from relName",
        # donc il est plus intéressant de mettre directement relName. 
        if (isinstance(self.expr, Rel)):
            expr_SQL = self.expr.relName

        # Pour les autres type d'expressions, on ne peut pas être sûr de la forme, donc on rajoute des ().
        else:
            expr_SQL = f"({expr_SQL})"

        return f"select distinct {', '.join(self.attrs)} from {expr_SQL}"