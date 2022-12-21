from Expressions.Expr import Expr
from sqlite3 import connect
from Expressions.InvalidExpression import tableDoesNotExistsError

class Rel(Expr):

    def __init__(self, relName: str):
        super().__init__()

        if (not isinstance(relName, str)):
            raise TypeError(f"The type of relName must be str, but is {type(relName).__name__}.")

        self.relName = relName
    
    def __str__(self) -> str:
        return f"Rel('{self.relName}')"
    
    def verify(self, db: str):
        
        # Permet de vérifier que relName est bien une table de db.
        if (len(self.findAttributes(db)) == 0):
            tableDoesNotExistsError(self, self.relName)

    def findAttributes(self, db: str) -> list:

        attributeDescriptions = connect(db).cursor().execute(f"PRAGMA table_info({self.relName})").fetchall()  

        for attr in attributeDescriptions:
            self.attributes[attr[1]] = attr[2]

        return self.attributes

    def toSQL(self, db: str) -> str:
        return f"select * from {self.relName}"