import json
import datetime
# noinspection PyUnresolvedReferences
from tinydb import TinyDB,Query,where

class ClassJoueurs:
    #def __init__(self, nom, prénom, date_naissance, sexe, classement, score_total, score_tournoi):
    def __init__(self, nom,prénom,date_naissance,sexe,classement,score_total,score_round):
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
        prénom = input("saisie prénom : \n")
        date_naissance = input ("date (format DD/MM/YYYY): \n")
        #date_naissance=input(datetime.datetime(2020,6,19))

        sexe = input("saisie sexe h ou f : \n" )
        classement = input("classement : \n")
        #score_total = input("score total : \n")
        #score_round = input("score round : \n")

        #Serialize l'instance joueurs
        joueur ={"nom":nom , "prénom":prénom, "date de naissance" : date_naissance,
                 "sexe" : sexe, "classement" : classement}

        #reconversion de l'instance sérialisée
        print("serialized nom")
        name=(joueur['nom'])
        print(name)

        return (joueur)
'''
        #Ecrire dans le fichier json fichier_joueur le contenu de joueur
        with open('data.json', 'w') as fichier_joueur:
            json.dump(joueur, fichier_joueur)
        print ("fichier_joueur")
        print(fichier_joueur)

        #lire le fichier data.json
        with open('data.json') as fichier_joueur:
            data = json.load(fichier_joueur)
            print("data")
            print(data)
        # TinyDB - Représente ta base de donnée
        # Query - Permet d'interroger ta base de donnée
        # where - Permet d'affiner tes critères de recherche
        from tinydb import TinyDB, Query, where
        Todo = Query()

        # Création de la table db_joueurs
        db_joueurs = TinyDB('db.json')

        # purge de la table
        #db_joueurs.truncate()

        # insertion des joueurs dans la table db_joueurs
        Prenom="test-prenom"
        db_joueurs.insert(
            {'nom': 'DUPONT', 'prénom': Prenom, 'date_naissance': '01/01/2000', 'sexe': 'f', 'classement': '100',
             'score_total': '2', 'score_round': '0.5'})
        db_joueurs.insert(
            {'nom': 'Duchnoc', 'prénom': 'Joe', 'date_naissance': '01/01/2010', 'sexe': 'h', 'classement': '02',
             'score_total': '0', 'score_round': '0'})



        print()
        return (joueur)
'''
