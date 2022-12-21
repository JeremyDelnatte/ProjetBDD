from Expressions.Expr import Expr

def schemaNotEqualError(expr, subExpr1, subExpr2, attrs1, attrs2):

    print("Invalid expression.", "The (sub-)expression", "  " + str(expr), "is invalid because the schema of", "  " + str(subExpr1), "which is", sep="\n")
    printSchema(attrs1)
    print("is not the same as the one from", "  " + str(subExpr2), "which is", sep="\n")
    printSchema(attrs2)

    exit()

def attributNotInSchemaError(expr, attr, subExpr, attrs):
    print("Invalid expression.", "The (sub-)expression", "  " + str(expr), "is invalid because the attribute", "  " + attr, "is not in the schema of", "  " + str(subExpr), "which is", sep="\n")
    printSchema(attrs)

    exit()

def sameAttributsDifferentTypeError(expr, attr, subExpr1, subExpr2, attrs1, attrs2):
    print("Invalid expression.", "The (sub-)expression", "  " + str(expr), "is invalid because the attribute", "  " + attr, sep="\n")
    print("is not the same in the schema of", "  " + str(subExpr1), "which is", sep="\n")
    printSchema(attrs1)
    print("as in the schema of", "  " + str(subExpr2), "which is", sep="\n")
    printSchema(attrs2)
    
    exit()

def differentTypeError(expr, attr1, attr2, subExpr, attrs):
    print("Invalid expression.", "The (sub-)expression", "  " + str(expr), "is invalid because the attributes", "  " + attr1 + " and " + attr2, sep="\n")
    print("don't have the same type in the schema of", "  " + str(subExpr), "which is", sep="\n")
    printSchema(attrs)

    exit()

def tableDoesNotExistsError(expr, relName):
    print("Invalid expression.", "The (sub-)expression", "  " + str(expr), "is invalid because the table", "  " + relName, "does not exists in the db.", sep="\n")
    
    exit()

def attributAlreadyExists(expr, name, subExpr, attrs):
    print("Invalid expression.", "The (sub-)expression", "  " + str(expr), "is invalid because the attribute", "  " + name, sep="\n")
    print("already exists in the schema of", "  " + str(subExpr), "which is", sep="\n")
    printSchema(attrs)

    exit()

def printSchema(attrs):

    for i, attr in enumerate(attrs):

        print(f"  '{attr}' {attrs[attr]}", end="")

        if (i != len(attrs) - 1):
            print(",")
        else:
            print()