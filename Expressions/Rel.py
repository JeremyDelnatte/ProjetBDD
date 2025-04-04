from Expressions.Expr import Expr
from sqlite3 import connect
from Expressions.InvalidExpression import tableDoesNotExistsError

class Rel(Expr):
    """
    Classe qui représente une relation en SPJRUD.

            Attributes:
                    attributes (dict): Le dictionnaire des attributs avec comme clé le nom et comme valeur le type de l'attribut
                    relName (str): Le nom de la relation
    """

    def __init__(self, relName: str):
        super().__init__()

        if (not isinstance(relName, str)):
            raise TypeError(f"The type of relName must be str, but is {type(relName).__name__}.")

        self.relName = relName
    
    def __str__(self) -> str:
        return f"Rel('{self.relName}')"
    
    def verify(self):
        
        # Permet de vérifier que relName est bien une table de db.
        if (len(self.attributes) == 0):
            tableDoesNotExistsError(self, self.relName)

    def findAttributes(self, db: str) -> list:

        attributeDescriptions = connect(db).cursor().execute(f"PRAGMA table_info({self.relName})").fetchall()  

        for attr in attributeDescriptions:
            self.attributes[attr[1]] = attr[2]

        return self.attributes

    def toSQL(self) -> str:
        return f"select distinct * from {self.relName}"