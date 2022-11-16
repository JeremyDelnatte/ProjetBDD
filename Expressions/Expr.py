from abc import ABC, abstractmethod

class Expr(ABC):
    
    db = None
    attributes = []

    @abstractmethod
    def toSQL(self) -> str:
        raise NotImplementedError("This is an abstract class, subclasses should implement this.")

    @abstractmethod
    def __init__(self):
        raise NotImplementedError("This is an abstract class, subclasses should implement this.")
    
    @abstractmethod
    def findAttributes(self, db: str) -> list:
        raise NotImplementedError("This is an abstract class, subclasses should implement this.")