import json
import datetime
import os

# noinspection PyUnresolvedReferences
from tinydb import TinyDB,Query,where

class ClassJoueurs:
    def __init__(self, id_joueur,nom,prénom,date_naissance,sexe,classement,score_total,score_round):
        self.id_joueur=id_joueur
        self.nom = nom
        self.prénom = prénom
        self.date_naissance = date_naissance
        self.sexe = sexe
        self.classement = classement
        self.score_total = score_total
        self.score_round = score_round

#Permet la création de tous les joueurs un par un, ils seront mis dans la bd par le contrôleur ou directement ici
    def CreatJoueurs(self):

        nom= input("saisie nom :\n")
        if nom=="":
            nom ="X"
            print("en absence de nom, le nom par défaut est \"X\"")
        if nom == "r":
            nom = "_x"
            print("r est un nom interdit, cela correspond à une commande clavier, le nom par défaut enregistré est \"_r\"")
        if nom=="E":
            nom = "_E"
            print("E est un nom interdit, cela correspond à une commande clavier, le nom par défaut enregistré est \"_E\"")

        prénom = input("saisie prénom : \n")
        date_naissance = input ("date (format DD/MM/YYYY): \n")
        #date_naissance=input(datetime.datetime(2020,6,19))

        sexe = input("saisie sexe h ou f : \n" )
        classement = input("classement : \n")

        # identifiant joueur
        import json
        from tinydb import TinyDB, Query, where
        Todo = Query()
        db_joueurs = TinyDB('joueurs.json')
        mode_ouv_fichier_json = "r"
        with open('joueurs.json', mode_ouv_fichier_json) as fichier_joueur:
            print("")

        #import operator
        db_joue = TinyDB('joueurs.json')

        #Rechercher un id libre dans la base de donnée en incrémentant l'id de test jusqu'à trouver un ID libre
        joueur_cherché = 1
        joueur_trouvé = 0
        id_libre=0

        #Si l' id_joueur_cherché n'est pas trouvé, on le prend pour le mettre à l'id du nouveau joueur
        #sinon, on reboucle jusqu'a trouver un id libre. On commence par regarder si l'id 1 existe
        joueur_trouvé = db_joueurs.search(Todo.id_joueur == joueur_cherché)
        joueur_trouv = str(joueur_trouvé)
        #recherche de la position de id_joueur dans la chaine
        char = 'id_joueur'
        PositDebNbre = (joueur_trouv.find(char))
        # recherche de la position de nom dans la chaine
        char = "nom"
        PositFinNbre = (joueur_trouv.find(char))

        #Recherche de l'id à partir des positions précédentes et suivantes'
        id_joueur = joueur_trouv[(PositDebNbre + 12): (PositFinNbre - 3)]
        print("id_joueur")
        print (id_joueur)

        #tant que l'id cherché existe, on recherche jusqu'à en trouver un libre en l'incrémentant
        while (id_joueur !=""):
            joueur_cherché = joueur_cherché + 1
            joueur_trouvé = db_joueurs.search(Todo.id_joueur == joueur_cherché)
            joueur_trouv = str(joueur_trouvé)
            char = 'id_joueur'
            PositDebNbre = (joueur_trouv.find(char))

            print("PositDebNbre")
            print(PositDebNbre)
            char = "nom"
            PositFinNbre = (joueur_trouv.find(char))
            print("PositFinNbre")
            print(PositFinNbre)

            id_joueur = joueur_trouv[(PositDebNbre + 12): (PositFinNbre - 3)]
            print("id_joueur")
            print(id_joueur)

        else:
            id_libre = joueur_cherché

        id_joueur=id_libre
        #Serialize l'instance joueurs
        joueur ={"id_joueur":id_joueur,"Nom":nom , "Prénom":prénom, "Date de naissance" : date_naissance,
                 "Sexe" : sexe, "Classement" : classement}

        #exemple de reconversion de l'instance sérialisée
        name = (joueur['Nom'])
        print("serialized nom pour exemple : " + name)
        print( "fin appel instance modele joueur de contrôleur joueur \n")
        return (joueur)
