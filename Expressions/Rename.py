from copy import deepcopy
from Expressions.Expr import Expr
from Expressions.Rel import Rel

class Rename(Expr):

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

    def findAttributes(self, db: str) -> list:
        
        if (db != self.db):
            self.db = db
            # On récupère les attributs et on change le nom de l'attribut attr par self.name.
            # Et on crée une liste avec seulement le nom des attributs qui va nous aider dans toSQL()
            self.attributes = deepcopy(self.expr.findAttributes(db))
            self.attributeNames = [attr[1] for attr in self.attributes]
            indexAttr = self.attributeNames.index(self.attr)
            self.attributes[indexAttr] = self.attributes[indexAttr][:1] + tuple(self.name) + self.attributes[indexAttr][2:]
            self.attributeNames[indexAttr] = f"{self.attr} '{self.name}'"

        return self.attributes


    def toSQL(self, db: str) -> str:
        expr_SQL = self.expr.toSQL(db)
        self.findAttributes(db)

        # Une expression Rel est sous forme "select * from relName",
        # donc il est plus intéressant de mettre directement relName. 
        if (isinstance(self.expr, Rel)):
            expr_SQL = self.expr.relName

        # Pour les autres type d'expressions, on ne peut pas être sûr de la forme, donc on rajoute des ().
        else:
            expr_SQL = f"({expr_SQL})"        

        return f"select {', '.join(self.attributeNames)} from {expr_SQL}"