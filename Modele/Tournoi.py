import json
import datetime
# noinspection PyUnresolvedReferences
from tinydb import TinyDB,Query,where

class ClassTournoi:
    def __init__(self, nom, lieu, date, nbr_rounds=4):
        self.nom = nom
        self.lieu = lieu
        self.date = date
        self.nbr_rounds = nbr_rounds

    def CreatTournois(self):
        nom= input("saisie nom : \n")
        if nom=="":
            nom ="X"
            print("en absence de nom, le nom par défaut est \"X\"")
        if nom == "r":
            nom = "_x"
            print("r est un nom interdit, cela correspond à une commande clavier, le nom par défaut enregistré est \"_r\"")
        if nom == "E":
            nom = "_E"
            print("E est un nom interdit, cela correspond à une commande clavier, le nom par défaut enregistré est \"_E\"")

        lieu = input("saisie lieu : \n")
        date = input("date (format DD/MM/YYYY): \n")

        nbr_rounds = input("saisie nombre de rounds, 4 rounds si pas de saisie: \n")
        if nbr_rounds =="":
            nbr_rounds ="4"

        # Serialize l'instance tournoi
        tournoi = {"nom": nom, "lieu": lieu, "date du tournoi": date,
                  "nombre de rounds": nbr_rounds}

        return (tournoi)
