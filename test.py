import sqlite3

from Expressions.Join import Join
from Expressions.Proj import Proj
from Expressions.Rel import Rel
from Expressions.Rename import Rename
from Expressions.Select import Cst, Select
from Expressions.Diff import Diff
from Expressions.Union import Union

from utilityFunctions import *

con = sqlite3.connect("test.db")
cur = con.cursor()

cur.execute("DROP TABLE IF EXISTS R")
cur.execute("""
    CREATE TABLE IF NOT EXISTS R( 
        A NUMERIC,
        B NUMERIC,
        C NUMERIC)""")

cur.execute("""
    INSERT INTO R VALUES
        (1, 3, 5),
        (4, 5, 2),
        (4, 5, 2)
""")

cur.execute("DROP TABLE IF EXISTS S")
cur.execute("""
    CREATE TABLE IF NOT EXISTS S( 
        A NUMERIC,
        B NUMERIC,
        C NUMERIC)""")

cur.execute("""
    INSERT INTO S VALUES
        (3, 5, 2),
        (4, 5, 2),
        (4, 5, 2)
 
""")

cur.execute("DROP TABLE IF EXISTS names")
cur.execute("""
    CREATE TABLE IF NOT EXISTS names( 
        eNom TEXT,
        id NUMERIC,
        testdefizofnez TEXT)""")

cur.execute("""
    INSERT INTO names VALUES
        ("Jérémy", 5, "dezfezfezf"),
        ("dedendejdei", 5, "dezdd"),
        (4, 5, 2)
 
""")

con.commit()


s = Select("A", "=", "C", Rel("R")).verify("test.db")
# printResultFromQuery(cur, s)
