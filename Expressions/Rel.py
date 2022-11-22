from Expressions.Expr import Expr
from sqlite3 import connect

class Rel(Expr):

    def __init__(self, relName: str):
        super().__init__()

        if (not isinstance(relName, str)):
            raise TypeError(f"The type of relName must be str, but is {type(relName).__name__}.")

        self.relName = relName
    
    def __str__(self) -> str:
        return f"Rel('{self.relName}')"

    def findAttributes(self, db: str) -> list:

        if (db != self.db):
            self.db = db
            self.attributes = connect(db).cursor().execute(f"PRAGMA table_info({self.relName})").fetchall()
            
        return self.attributes

    def toSQL(self, db: str) -> str:
        return f"select * from {self.relName}"