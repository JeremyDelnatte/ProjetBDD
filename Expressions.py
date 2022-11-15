class Expr:
    pass


class Rel(Expr):

    def __init__(self, relName: str):

        if (not isinstance(relName, str)):
            raise TypeError(f"The type of relName must be str and have a length of at least 1.")

        self.relName = relName
    
    def __str__(self) -> str:
        return f"Rel('{self.relName}')"


class Cst:

    def __init__(self, cst: str):

        if (not isinstance(cst, str) or len(cst) < 1):
            raise TypeError(f"The type of cst must be str and have a length of at least 1.")

        self.cst = cst
    
    def __len__(self) -> int:
        return len(self.cst)

    def __str__(self) -> str:
        return f"Cst('{self.cst}')"


class Select(Expr):

    def __init__(self, attr1: str, operator: str, attr2, expr: Expr):
        if (not isinstance(attr1, str) or len(attr1) < 1):
            raise TypeError(f"The type of attr1 must be str and have a length of at least 1.")
        
        elif (not isinstance(operator, str) or operator != "="):
            raise TypeError(f"The type of operator must be str and be '='.")
        
        elif (not isinstance(attr2, (str, Cst)) or len(attr2) < 1):
            raise TypeError(f"The type of attr2 must be str or Cst and have a length of at least 1.")

        elif (not isinstance(expr, Expr)):
            raise TypeError(f"The type of expr must be Expr.")
        
        self.attr1 = attr1
        self.attr2 = attr2
        self.operator = operator
        self.expr = expr

    def __str__(self) -> str:
        attr2String = str(self.attr2) if isinstance(self.attr2, Cst) else f"'{self.attr2}'"
        return f"Select('{self.attr1}', '{self.operator}', {attr2String}, {str(self.expr)})"


class Rename(Expr):

    def __init__(self, attr: str, name: str, expr: Expr):
        if (not isinstance(attr, str) or len(attr) < 1):
            raise TypeError(f"The type of attr must be str and have a length of at least 1.")
        
        elif (not isinstance(name, str) or len(name) < 1):
            raise TypeError(f"The type of name must be str and have a length of at least 1.")
        
        elif (not isinstance(expr, Expr)):
            raise TypeError(f"The type of expr must be Expr.")
        
        self.attr = attr
        self.name = name
        self.expr = expr

    def __str__(self) -> str:
        return f"Rename('{self.attr}', '{self.name}', {str(self.expr)})"
    

class Join(Expr):

    def __init__(self, expr1: Expr, expr2: Expr):
        
        if (not isinstance(expr1, Expr)):
            raise TypeError(f"The type of expr1 must be Expr.")
        
        elif (not isinstance(expr2, Expr)):
            raise TypeError(f"The type of expr2 must be Expr.")

        self.expr1 = expr1
        self.expr2 = expr2

    def __str__(self) -> str:
        return f"Join({str(self.expr1)}, {str(self.expr2)})"


class Proj(Expr):

    def __init__(self, attrs: list[str], expr: Expr):
        if (not isinstance(attrs, list) or not all(isinstance(attr, str) and len(attr) > 0 for attr in attrs) or len(attrs) < 1):
            raise TypeError(f"The type of attrs must be list[str] and have a length of at least 1.")
        
        elif (not isinstance(expr, Expr)):
            raise TypeError(f"The type of expr must be Expr.")
        
        self.attrs = attrs
        self.expr = expr

    def __str__(self) -> str:
        return f"Proj({self.attrs}, {str(self.expr)})"