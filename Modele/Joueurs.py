import json

# noinspection PyUnresolvedReferences
from tinydb import TinyDB,Query,where

db = TinyDB('db.json')
db.insert({'type': 'apple', 'count': 7})
db.insert({'type': 'peach', 'count': 3})

#print(db.all())

print()
#print (db.all)

#TinyDB - Représente ta base de donnée
#Query - Permet d'interroger ta base de donnée
#where - Permet d'affiner tes critères de recherche



#db = TinyDB('db.json')
#db_joueurs = db.table('joueurs')
#db_joueurs.insert(joueur)
'''
from tinydb import TinyDB, Query
from pprint import pprint

db = TinyDB('db.json')
fruits = db.table('fruits')

fruits.insert({'type': 'fraise', 'quantite': 4})
fruits.insert({'type': 'orange', 'quantite': 1})
fruits.insert({'type': 'banane', 'quantite': 7})

pprint(fruits.all())
#[{'quantite': 4, 'type': 'fraise'},
#{'quantite': 1, 'type': 'orange'},
#{'quantite': 7, 'type': 'banane'}]

fichier db.json:
{"fruits": {"1": {"type": "fraise", "quantite": 4}, "2": {"type": "orange", "quantite": 1}, "3": {"type": "banane", "quantite": 7}}}
'''


class Joueurs:
    #def __init__(self, nom, prénom, date_naissance, sexe, classement, score_total, score_tournoi):
    def __init__(self, nom,prénom,date_naissance,sexe,classement,score_total,score_round):
        self.nom = nom
        self.prénom = prénom
        self.date_naissance = date_naissance
        self.sexe = sexe
        self.classement = classement
        self.score_total = score_total
        self.score_round = score_round


    def CreatJoueurs(self):
        nom= input("saisie nom : ")
        prénom = input("saisie prénom : ")
        date_naissance = input("date : ")
        sexe = input("saisie sexe h ou f : " )
        classement = input("classement : ")
        #score_total = input("score total : ")
        #score_round = input("score round : ")

        print()
        print("nom: " + nom)
        print("prénom : " + prénom)
        print("date de naissance : " + date_naissance)
        print("sexe : " + sexe)
        print("classement : " + classement)
        #print("score total : " + score_total)
        #print("score round : " + score_round)

        joueur ={"nom_1":nom , "prénom_1 ":prénom, "date de naissance_1 : " : date_naissance,
                 "sexe_1  : " : sexe, "classement_1  : " : classement}

        #Ecrire dans le fichier json fichier_joueur le contenu de joueur
        with open('data.json', 'w') as fichier_joueur:
            json.dump(joueur, fichier_joueur)

        with open('data.json') as fichier_joueur:
            data = json.load(fichier_joueur)

            print(data)
            #print(data.nom_1)
            #print(data.nom_1)
        return ()


