from abc import ABC, abstractmethod

# This is an abstract class.
class Expr(ABC):
    """
    Classe abstraite.
    Classe qui représente une expression en SPJRUD.

            Attributes:
                    attributes (dict): Le dictionnaire des attributs avec comme clé le nom et comme valeur le type de l'attribut
    """

    @abstractmethod
    def toSQL(self) -> str:
        """
        Permet de traduire l'expression en une requête SQL. 

                Preconditions:
                        Il faut avoir appelé findAttributes() avant pour définir les attributs.
                        Et il faut aussi avoir appelé verify() avant car sinon aucune vérification sera faite.

                Returns:
                        str : La requête SQL
        """
        raise NotImplementedError("This is an abstract class, subclasses should implement this.")

    def __init__(self):
        """
        Permet d'ajouter tous les attributs et vérifie que leurs types sont correcte, sinon raise un TypeError.
        """
        self.attributes = {}

    @abstractmethod
    def findAttributes(self, db: str) -> dict:
        """
        Permet de calculer les attributs de l'expression. 

                Parameters:
                        db (str): La base de données

                Returns:
                        dict : Le dictionnaire des attributs avec comme clé le nom et comme valeur le type de l'attribut
        """
        raise NotImplementedError("This is an abstract class, subclasses should implement this.")
    
    @abstractmethod
    def verify(self):
        """
        Permet de vérifier que l'expression est correcte. 

                Preconditions:
                        Il faut avoir appelé findAttributes() avant pour définir les attributs.

                Returns:
                        None
        """
        raise NotImplementedError("This is an abstract class, subclasses should implement this.")

    @abstractmethod
    def __str__(self) -> str:
        """
        Permet de convertir l'expression en une chaîne de caractères. 

                Returns:
                        str : L'expression converti en chaîne de caractères.
        """
        raise NotImplementedError("This is an abstract class, subclasses should implement this.")