
import datetime
import os

def creat_dict(donnees_db):
    #D1 = {'1': "A", '2': "B", '3': 23}
    str_donnees = str(donnees_db)

    str_donnees = str_donnees.replace("[", "")
    str_donnees = str_donnees.replace("]", "")


    #print("str_donnees")
    #print(str_donnees)
    import ast
    try:
        dict_donnees = ast.literal_eval(str_donnees)

    except SyntaxError:
        print("")
        print("Le tournoi est déjà chargé avec des rounds, supprimer et recréer ce tournoi pour le recharger")
        os._exit(0)

    #dict_donnees = ast.literal_eval(str_donnees)
    return (dict_donnees)

def tournoi_exist(id_tournoi_select):
    from tinydb import TinyDB, Query, where
    Todo = Query()
    db_tournois = TinyDB('tournois.json')
    print("db_tournois.search(where('id_tournoi')==id_tournoi_select")
    int_tournoi_select = int(id_tournoi_select)

    # charger le tournoi selectionné à partir de la table dans tournoi
    try:
        trouve_tournoi = (db_tournois.search(where('id_tournoi') == int_tournoi_select))
    except :
        trouve_tournoi=""
        print("tournoi introuvable ")
        os._exit(0)

    return (trouve_tournoi)

def creat_list(donnees_db):
    str_donnees = str(donnees_db)
    str_donnees = str_donnees.replace("{", "")
    str_donnees = str_donnees.replace("}", "")
    liste_donnees = str_donnees

    return (liste_donnees)
