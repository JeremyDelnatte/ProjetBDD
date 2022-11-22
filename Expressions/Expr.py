from abc import ABC, abstractmethod

# This is an abstract class.
class Expr(ABC):

    @abstractmethod
    def toSQL(self, db: str) -> str:
        raise NotImplementedError("This is an abstract class, subclasses should implement this.")

    def __init__(self):
        self.db = None
        self.attributes = []

        # print(__class__)

        # raise NotImplementedError("This is an abstract class, subclasses should implement this.")
    
    @abstractmethod
    def findAttributes(self, db: str) -> list:
        raise NotImplementedError("This is an abstract class, subclasses should implement this.")