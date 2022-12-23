from abc import ABC, abstractmethod

# This is an abstract class.
class Expr(ABC):

    @abstractmethod
    def toSQL(self) -> str:
        raise NotImplementedError("This is an abstract class, subclasses should implement this.")

    def __init__(self):
        self.attributes = {}

    @abstractmethod
    def findAttributes(self, db: str) -> dict:
        raise NotImplementedError("This is an abstract class, subclasses should implement this.")
    
    @abstractmethod
    def verify(self):
        raise NotImplementedError("This is an abstract class, subclasses should implement this.")