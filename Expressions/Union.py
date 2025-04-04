from copy import deepcopy
from Expressions.Expr import Expr
from Expressions.Rel import Rel
from Expressions.InvalidExpression import schemaNotEqualError

class Union(Expr):
    """
    Classe qui représente l'opérateur Union en SPJRUD.

            Attributes:
                    attributes (dict): Le dictionnaire des attributs avec comme clé le nom et comme valeur le type de l'attribut
                    expr1 (Expr): La sous expression 1
                    expr2 (Expr): La sous expression 2
    """

    def __init__(self, expr1: Expr, expr2: Expr):
        super().__init__()

        if (not isinstance(expr1, Expr)):
            raise TypeError(f"The type of expr1 must be Expr, but is {type(expr1).__name__}.")
        
        elif (not isinstance(expr2, Expr)):
            raise TypeError(f"The type of expr2 must be Expr, but is {type(expr2).__name__}.")

        self.expr1 = expr1
        self.expr2 = expr2

    def __str__(self) -> str:
        return f"Union({str(self.expr1)}, {str(self.expr2)})"
    
    def verify(self):
        
        self.expr1.verify()
        self.expr2.verify()

        attrs1 = self.expr1.attributes
        attrs2 = self.expr2.attributes

        if (len(attrs1) != len(attrs2)):
            schemaNotEqualError(self, self.expr1, self.expr2, attrs1, attrs2)

        # Permet de vérifier que tous les attributs de expr1 sont aussi des attributs de expr2
        for key in attrs1:
            if (key not in attrs2 or attrs1[key] != attrs2[key]):
                schemaNotEqualError(self, self.expr1, self.expr2, attrs1, attrs2)

    def findAttributes(self, db: str) -> list:
        
        # Pas besoin de faire une vérification ici car cela va être fait dans la vérification par après.
        self.attributes = deepcopy(self.expr1.findAttributes(db))
        self.expr2.findAttributes(db)
        return self.attributes

    def toSQL(self) -> str:
        expr1_SQL = self.expr1.toSQL()
        expr2_SQL = self.expr2.toSQL()

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

        return f"select * from {expr1_SQL} union select * from {expr2_SQL}"