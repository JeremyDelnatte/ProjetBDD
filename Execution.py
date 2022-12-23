from Expressions.Expr import Expr
from sqlite3 import Cursor

def toSQL(request: Expr, db: str) -> str:
    request.findAttributes(db)
    request.verify()
    return request.toSQL()

def verify(request: Expr, db: str):
    request.findAttributes(db)
    request.verify()

# Précondition : la base de données du cursor est la même que db.
def executeRequest(request: Expr, db: str, cur: Cursor) -> list:
    return cur.execute(toSQL(request, db)).fetchall()
