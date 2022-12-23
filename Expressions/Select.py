from copy import deepcopy
from Expressions.Expr import Expr
from Expressions.Rename import Rename
from Expressions.Rel import Rel
from Expressions.Proj import Proj
from Expressions.InvalidExpression import attributNotInSchemaError, differentTypeError

class Cst:
    """
    Classe qui représente une constante pour l'opérateur Select en SPJRUD.

            Attributes:
                    cst (str): La constante
    """

    def __init__(self, cst: str):

        if (not isinstance(cst, str)):
            raise TypeError(f"The type of cst must be str, but is {type(cst).__name__}.")

        self.cst = cst

    def __str__(self) -> str:
        """
        Permet de convertir la constante en une chaîne de caractères. 

                Returns:
                        str : self converti en chaîne de caractères.
        """
        return f"Cst('{self.cst}')"

class Select(Expr):
    """
    Classe qui représente l'opérateur Select en SPJRUD.

            Attributes:
                    attributes (dict): Le dictionnaire des attributs avec comme clé le nom et comme valeur le type de l'attribut
                    attr1 (str): L'attribut à gauche de l'operateur
                    operator (str): L'opérateur
                    attr2 (str or Cst): Soit une constante ou soit un attribut à droite de l'opérateur
                    expr (Expr): La sous expression
    """

    def __init__(self, attr1: str, operator: str, attr2, expr: Expr):
        super().__init__()
        
        if (not isinstance(attr1, str)):
            raise TypeError(f"The type of attr1 must be str, but is {type(attr1).__name__}.")
        
        elif (operator not in ("=", "<", "<=", ">", ">=")):
            raise TypeError("Operator must be '=', '<', '<=', '>', '>='.")
        
        elif (not isinstance(attr2, (str, Cst))):
            raise TypeError(f"The type of attr2 must be str or Cst, but is {type(attr2).__name__}.")

        elif (not isinstance(expr, Expr)):
            raise TypeError(f"The type of expr must be Expr, but is {type(expr).__name__}.")
        
        self.attr1 = attr1
        self.attr2 = attr2
        self.operator = operator
        self.expr = expr

    def __str__(self) -> str:
        attr2String = str(self.attr2) if isinstance(self.attr2, Cst) else f"'{self.attr2}'"
        return f"Select('{self.attr1}', '{self.operator}', {attr2String}, {str(self.expr)})"  

    def verify(self):
        
        self.expr.verify()

        attrs = self.expr.attributes

        # Permet de vérifier que self.attr1 existe bien en tant qu'attribut de self.expr.
        if (self.attr1 not in attrs):
            attributNotInSchemaError(self, self.attr1, self.expr, attrs)
        
        # Si self.attr2 est de type str, cela signifie que c'est un attribut et pas une constante.
        if (isinstance(self.attr2, str)):

            # Permet de vérifier que self.attr2 existe bien en tant qu'attribut de self.expr.
            if (self.attr2 not in attrs):
                attributNotInSchemaError(self, self.attr2, self.expr, attrs)

            # Permet de vérifier que self.attr1 et self.attr2 ont bien le même type.
            if (attrs[self.attr1] != attrs[self.attr2]):
                differentTypeError(self, self.attr1, self.attr2, self.expr, attrs)

    def findAttributes(self, db: str) -> list:

        # Pas besoin de faire une vérification ici car cela va être fait dans la vérification par après.
        self.attributes = deepcopy(self.expr.findAttributes(db))
        return self.attributes


    def toSQL(self) -> str:
        expr_SQL = self.expr.toSQL()

        # Si attr2 est une constante, on ajoute des ''.
        attr2_SQL = f"'{self.attr2.cst}'" if isinstance(self.attr2, Cst) else self.attr2

        # Les expressions Rel, Rename, Proj sont déjà sous la forme "select ... from ..."
        if (not isinstance(self.expr, (Rel, Rename, Proj))):
            expr_SQL = f"select * from ({expr_SQL})"

        return expr_SQL + f" where {self.attr1} {self.operator} {attr2_SQL}"
    
