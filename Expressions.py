import sqlite3


class Expr:
    pass


class Rel(Expr):

    def __init__(self, relName: str):

        if (not isinstance(relName, str)):
            raise TypeError("The type of relName must be str and have a length of at least 1.")

        self.relName = relName
    
    def __str__(self) -> str:
        return f"Rel('{self.relName}')"
    
    def toSQL(self, db: str) -> str:
        schema = sqlite3.connect(db).cursor().execute(f"PRAGMA table_info({self.relName})").fetchall()
        column_list = [column[1] for column in schema]
        return (f"select * from {self.relName}", column_list)


class Cst:

    def __init__(self, cst: str):

        if (not isinstance(cst, str) or len(cst) < 1):
            raise TypeError("The type of cst must be str and have a length of at least 1.")

        self.cst = cst
    
    def __len__(self) -> int:
        return len(self.cst)

    def __str__(self) -> str:
        return f"Cst('{self.cst}')"

    def toSQL(self) -> str:
        return f"'{self.cst}'"


class Select(Expr):

    def __init__(self, attr1: str, operator: str, attr2, expr: Expr):
        if (not isinstance(attr1, str) or len(attr1) < 1):
            raise TypeError("The type of attr1 must be str and have a length of at least 1.")
        
        elif (not isinstance(operator, str) or operator != "="):
            raise TypeError("The type of operator must be str and be '='.")
        
        elif (not isinstance(attr2, (str, Cst)) or len(attr2) < 1):
            raise TypeError("The type of attr2 must be str or Cst and have a length of at least 1.")

        elif (not isinstance(expr, Expr)):
            raise TypeError("The type of expr must be Expr.")
        
        self.attr1 = attr1
        self.attr2 = attr2
        self.operator = operator
        self.expr = expr

    def __str__(self) -> str:
        attr2String = str(self.attr2) if isinstance(self.attr2, Cst) else f"'{self.attr2}'"
        return f"Select('{self.attr1}', '{self.operator}', {attr2String}, {str(self.expr)})"

    def toSQL(self, db: str) -> str:
        attr2SQL = self.attr2.toSQL() if isinstance(self.attr2, Cst) else self.attr2
        exprSQL, column_list = self.expr.toSQL(db)

        if (not isinstance(self.expr, Rel)):
            exprSQL = f"select * from ({exprSQL})"

        return (exprSQL + f" where {self.attr1 + self.operator + attr2SQL}", column_list)


class Rename(Expr):

    def __init__(self, attr: str, name: str, expr: Expr):
        if (not isinstance(attr, str) or len(attr) < 1):
            raise TypeError("The type of attr must be str and have a length of at least 1.")
        
        elif (not isinstance(name, str) or len(name) < 1):
            raise TypeError("The type of name must be str and have a length of at least 1.")
        
        elif (not isinstance(expr, Expr)):
            raise TypeError("The type of expr must be Expr.")
        
        self.attr = attr
        self.name = name
        self.expr = expr

    def __str__(self) -> str:
        return f"Rename('{self.attr}', '{self.name}', {str(self.expr)})"

    def toSQL(self, db: str) -> str:
        exprSQL, column_list = self.expr.toSQL(db)

        print(column_list)

        if (self.attr not in column_list):
            raise Exception("Trying to rename a column that doesn't exist.")

        column_list_str = ""
        for i in range(len(column_list)):

            if (column_list[i] == self.attr):
                column_list[i] = self.name
                column_list_str += f"{self.attr} '{self.name}', "
            
            else:
                column_list_str += f"{column_list[i]}, "
        
        column_list_str = column_list_str[:-2]

        if (not isinstance(self.expr, Rel)):
            exprSQL = f"({exprSQL})"
        else: 
            exprSQL = self.expr.relName

        return (f"select {column_list_str} from {exprSQL}", column_list)

    

class Join(Expr):

    def __init__(self, expr1: Expr, expr2: Expr):
        
        if (not isinstance(expr1, Expr)):
            raise TypeError("The type of expr1 must be Expr.")
        
        elif (not isinstance(expr2, Expr)):
            raise TypeError("The type of expr2 must be Expr.")

        self.expr1 = expr1
        self.expr2 = expr2

    def __str__(self) -> str:
        return f"Join({str(self.expr1)}, {str(self.expr2)})"
    
    def toSQL(self, db: str) -> str:
        expr1_SQL, columns_list1 = self.expr1.toSQL(db)
        expr2_SQL, columns_list2 = self.expr2.toSQL(db)

        if (not isinstance(self.expr1, Rel)):
            expr1_SQL = f"({expr1_SQL})"
        else:
            expr1_SQL = self.expr1.relName

        if (not isinstance(self.expr2, Rel)):
            expr2_SQL = f"({expr2_SQL})"
        else:
            expr2_SQL = self.expr2.relName

        columns_list = []
        intersect_list = []
        for col in columns_list1:
            if (col in columns_list2):
                intersect_list.append(col)
            columns_list.append(col)

        print(intersect_list)
        
        for col in columns_list2:
            if (col not in columns_list):
                columns_list.append(col)

        if (len(intersect_list) == 0):
            return (f"select * from {expr1_SQL} cross join {expr2_SQL}", columns_list)
        
        elif (len(columns_list) > len(intersect_list)):

            columns = []
            for col in columns_list1:
                columns.append("R." + col)

            for col in columns_list2:
                if (col not in intersect_list):
                    columns.append("S." + col)

            str_columns = ", ".join(columns)

            condition = []
            for col in intersect_list:
                condition.append(f"R.{col}=S.{col}")

            return (f"select {str_columns} from {expr1_SQL} as 'R' join {expr2_SQL} as 'S' on {' and '.join(condition)}", columns_list)

        else:
            return (f"select * from {expr1_SQL} intersect select * from {expr2_SQL}", columns_list)



class Proj(Expr):

    def __init__(self, attrs: list[str], expr: Expr):
        if (not isinstance(attrs, list) or not all(isinstance(attr, str) and len(attr) > 0 for attr in attrs) or len(attrs) < 1):
            raise TypeError("The type of attrs must be list[str] and have a length of at least 1.")
        
        elif (not isinstance(expr, Expr)):
            raise TypeError("The type of expr must be Expr.")
        
        self.attrs = attrs
        self.expr = expr

    def __str__(self) -> str:
        return f"Proj({self.attrs}, {str(self.expr)})"
    
    def toSQL(self, db: str) -> str:
        pass
