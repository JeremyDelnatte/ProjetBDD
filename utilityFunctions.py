import sqlite3


def createTableFromQuery(query: str, tableName: str, db: str):
    """
    Permet de créer un table à partir d'une requête SQL. Si la table existe, l'ancienne table est écrasé.

            Parameters:
                    query (str): La requête SQL
                    tableName (str): Le nom de la nouvelle table
                    db (str): Le fichier de la base de données

            Returns:
                    None
    """

    con = sqlite3.connect(db)
    cur = con.cursor()

    cur.execute(f"DROP TABLE IF EXISTS {tableName}")
    cur.execute(f"CREATE TABLE {tableName} as {query}")
    con.commit()

def printResultFromQuery(query: str, db: str):
    """
    Permet d'afficher le resultat d'une requête SQL.

            Parameters:
                    query (str): La requête SQL
                    db (str): Le fichier de la base de données

            Returns:
                    None
    """

    cur = sqlite3.connect(db).cursor()

    cur.execute(query)
    attributeNames = [attr[0] for attr in cur.description]
    result = cur.fetchall()

    # Permet de trouver la taille max de toutes les colonnes
    maxLength = [len(name) for name in attributeNames]
    for res in result:
        for i in range(len(attributeNames)):
            
            if (maxLength[i] < len(str(res[i]))):
                maxLength[i] = len(str(res[i]))
    
    # Permet de mettre la taille de tous les élements d'une colonne à la taille max de la colonne
    for i in range(len(result)):
        l = []
        for j in range(len(attributeNames)):
            l.append(f"%{maxLength[j]}s" % str(result[i][j]))
        
        result[i] = tuple(l)

    # Permet de mettre la taille de tous les noms de colonnes à la taille max de la colonne
    attributeNames = [f"%{maxLength[i]}s" % attributeNames[i] for i in range(len(attributeNames))]

    
    # Affiche le résultat
    line = f"+-{'-+-'.join(['-'*maxLen for maxLen in maxLength])}-+"
    print(line)
    print(f"| {' | '.join(attributeNames)} |")
    print(line)

    for res in result:
        print(f"| {' | '.join(res)} |")

    print(line)