# print(Proj(["Population"], 
#     Join(Rename("Name", "Capital", Rel("Cities")),
#     Select("Country", "=", Cst("Mali"), Rel("CC")))))

import sqlite3

from Expressions.Join import Join
from Expressions.Proj import Proj
from Expressions.Rel import Rel
from Expressions.Rename import Rename
from Expressions.Select import Select

con = sqlite3.connect("test.db")
cur = con.cursor()
cur.execute("""
    CREATE TABLE IF NOT EXISTS R( 
        A NUMERIC,
        B NUMERIC,
        C NUMERIC)""")

cur.execute("delete from R")
cur.execute("""
    INSERT INTO R VALUES
        (1, 3, 5),
        (4, 5, 2),
        (4, 5, 2)
""")

cur.execute("""
    CREATE TABLE IF NOT EXISTS S( 
        A NUMERIC,
        B NUMERIC,
        C NUMERIC)""")

cur.execute("delete from S")
cur.execute("""
    INSERT INTO S VALUES
        (3, 5, 2),
        (4, 5, 2)
 
""")

con.commit()

# print(cur.execute("select R.A, R.B, R.C, S.D from (select * from R) as 'R' join (select * from S) as 'S' on R.B = S.B and R.C = S.C").fetchall()) # join
# print(cur.execute("select R.A, R.B, R.C, S.D from R join S as 'S' on R.B = S.B and R.C = S.C").fetchall()) # join
# print(cur.execute("select * from R union select * from S").fetchall()) # union
# print(cur.execute("select distinct A, B from R").fetchall()) # project
# print(cur.execute("select * from R where A='1'").fetchall()) # select
# print(cur.execute("select A 'D', B, C from R").fetchall()) # rename
# print(cur.execute("select * from R natural join S").fetchall())

# print(cur.execute("select R.A, R.B, R.C, S.D from R as 'R' join S as 'S' on R.C=S.C and R.B=S.B").fetchall())

# l = cur.execute("PRAGMA table_info(R)").fetchall()
# names = [column[1] for column in l]

# print(names)

# print(cur.execute("select * from R intersect select * from S").fetchall())
# print(cur.execute("select * from R natural join S").fetchall())

# Rel
# Select
# Proj 
# Join
# Rename
# TODO Union
# TODO Diff

print(Join(Rel("R"), Rel("S")).toSQL("test.db"))
print(Join(Rel("R"), Rename("A", "E", Rel("S"))).toSQL("test.db"))