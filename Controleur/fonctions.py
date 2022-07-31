
import datetime

def creat_dict(donnees_db):
    D1 = {'1': "A", '2': "B", '3': 23}
    str_donnees = str(donnees_db)
    str_donnees = str_donnees.replace("[", "")
    str_donnees = str_donnees.replace("]", "")
    import ast
    dict_donnees = ast.literal_eval(str_donnees)
    return (dict_donnees)

