from copy import deepcopy
from Expressions.Expr import Expr
from Expressions.Rel import Rel
from Expressions.InvalidExpression import attributNotInSchemaError, attributAlreadyExists

class Rename(Expr):
    """
    Classe qui représente l'opérateur Rename en SPJRUD.

            Attributes:
                    attributes (dict): Le dictionnaire des attributs avec comme clé le nom et comme valeur le type de l'attribut
                    attr (str): L'attribut qui va être renommer
                    name(str): Le nom qui va être donné à l'attribut attr
                    expr (Expr): La sous expression
    """

    def __init__(self, attr: str, name: str, expr: Expr):
        super().__init__()
        
        if (not isinstance(attr, str)):
            raise TypeError(f"The type of attr must be str, but is {type(attr).__name__}.")
        
        elif (not isinstance(name, str)):
            raise TypeError(f"The type of name must be str, but is {type(name).__name__}.")
        
        elif (not isinstance(expr, Expr)):
            raise TypeError(f"The type of expr must be Expr, but is {type(expr).__name__}.")
        
        self.attr = attr
        self.name = name
        self.expr = expr

    def __str__(self) -> str:
        return f"Rename('{self.attr}', '{self.name}', {str(self.expr)})"

    def verify(self):
        
        self.expr.verify()

        attrs = self.expr.attributes

        if (self.attr not in attrs):
            attributNotInSchemaError(self, self.attr, self.expr, attrs)

        elif (self.name in attrs):
            attributAlreadyExists(self, self.name, self.expr, attrs)

    def findAttributes(self, db: str) -> dict:
        
        self.attributes = deepcopy(self.expr.findAttributes(db))

        # On ne vérifie pas si l'attribut existe ou non mais cela va être vérifier après lors du verify()
        # Permet de garder le même ordre.
        try:
            index = list(self.attributes.keys()).index(self.attr)
            items = list(self.attributes.items())
            items[index] = (self.name, self.attributes[self.attr])
            self.attributes = dict(items)

        # On ne fait rien car par près lors du verify() une erreur va être lancé.
        except ValueError:
            pass
            
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

        attrs = list(self.attributes.keys())
        attrs[attrs.index(self.name)] = f"{self.attr} '{self.name}'"    

        return f"select distinct {', '.join(attrs)} from {expr_SQL}"