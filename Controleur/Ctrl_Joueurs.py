"""création des joueurs - appel du modele joueur lors de la création des joueurs"""
"""affichage liste joueurs de la base de donnée, suppression d'un joueur de la base de donnée, purge de la base de donnée"""
import os
import re
from Vue.menu import ClassMainMenu
from Modele.Joueurs import ClassJoueurs
from Vue.affichage import ClassVueAffichage

import json
from tinydb import TinyDB, Query, where
Todo = Query()
db_joueurs = TinyDB('joueurs.json')

def creat_new_joueurs():
        # CREATION DE L'ID DU JOUEUR ************************************
        from tinydb import TinyDB, Query
        Todo = Query()
        db_joueurs = TinyDB('joueurs.json')
        mode_ouv_fichier_json = "r"
        with open('joueurs.json', mode_ouv_fichier_json) as fichier_joueur:
                pass

        # import operator
        db_joue = TinyDB('joueurs.json')  # A SUPPRIMER

        # Rechercher un id libre dans la base de donnée en incrémentant l'id de test jusqu'à trouver un ID libre
        joueur_cherche = 1
        joueur_trouve = 0
        id_libre = 0

        # Si l' id_joueur_cherché n'est pas trouvé, on le prend pour le mettre à l'id du nouveau joueur
        # sinon, on reboucle jusqu'a trouver un id libre. On commence par regarder si l'id 1 existe
        joueur_trouve = db_joueurs.search(Todo.id_joueur == joueur_cherche)
        joueur_trouv = str(joueur_trouve)
        # recherche de la position de id_joueur dans la chaine
        char = 'id_joueur'
        PositDebNbre = (joueur_trouv.find(char))
        # recherche de la position de nom dans la chaine
        char = "nom"
        PositFinNbre = (joueur_trouv.find(char))

        # Recherche de l'id à partir des positions précédentes et suivantes'
        id_joueur = joueur_trouv[(PositDebNbre + 12): (PositFinNbre - 3)]

        # tant que l'id cherché existe, on recherche jusqu'à en trouver un libre en l'incrémentant
        while (id_joueur != ""):
                joueur_cherche = joueur_cherche + 1
                joueur_trouve = db_joueurs.search(Todo.id_joueur == joueur_cherche)
                joueur_trouv = str(joueur_trouve)
                char = 'id_joueur'
                PositDebNbre = (joueur_trouv.find(char))

                char = "nom"
                PositFinNbre = (joueur_trouv.find(char))

                id_joueur = joueur_trouv[(PositDebNbre + 12): (PositFinNbre - 3)]

        else:
                id_libre = joueur_cherche

        print (id_libre)

        #self=""
        #inst_creat_joueurs = ClassJoueurs.CreatJoueurs(self.__class__)

        wd = os.getcwd() #récupération du chemin
        #print (wd)

        working_directory = str(wd)
        working_directory_db = working_directory + "/joueurs.json"
        mode_ouv_fichier_json = "a+"
        with open('joueurs.json', mode_ouv_fichier_json) as fichier_joueur:
                pass
        #***************************************************************************************
        nom = ClassVueAffichage.Input(self=True,texte1="saisie nom :")
        if nom == "":
                nom = ("Joueur " + str(id_libre))
                ClassVueAffichage.Affichage(self=True,texte1="en absence de nom, le nom par défaut est " + nom,texte2="",texte3="")
        if nom == "r":
                nom = ("Joueur " + str(id_libre))
                ClassVueAffichage.Affichage(self=True, texte1="r est un nom interdit, cela correspond à une commande clavier, le nom par défaut est " + nom,
                                            texte2="", texte3="")
        if nom == "E":
                nom = ("Joueur " + str(id_libre))
                ClassVueAffichage.Affichage(self=True,
                                            texte1="E est un nom interdit, cela correspond à une commande clavier, le nom par défaut enregistré est " + nom,
                                            texte2="", texte3="")

        prenom = ClassVueAffichage.Input(self=True, texte1="saisie prénom :")
        if prenom == "":
                prenom = ("Prenom " + str(id_libre))
                ClassVueAffichage.Affichage(self=True,texte1="en absence de prenom, le prenom par défaut est " + prenom,texte2="",texte3="")
        if prenom == "r":
                prenom = ("Prenom " + str(id_libre))
                ClassVueAffichage.Affichage(self=True,
                                            texte1="r est un nom interdit, cela correspond à une commande clavier, le prenom par défaut est " + prenom,
                                            texte2="", texte3="")
        if prenom == "E":
                prenom = ("Prenom " + str(id_libre))
                ClassVueAffichage.Affichage(self=True,texte1="E est un nom interdit, cela correspond à une commande clavier, le prenom par défaut enregistré est " + prenom,
                                            texte2="", texte3="")

        date_naissance = ClassVueAffichage.Input(self=True, texte1="date de naissance (format DD/MM/YYYY):")
        if date_naissance == "":
                date_naissance = "01-01-1900"

        sexe = ClassVueAffichage.Input(self=True, texte1="saisie sexe h ou f ou nc :")
        #sexe = input("saisie sexe h ou f ou nc : \n")
        assertions = ["H", "h", "F", "f"]
        if sexe == "":
                sexe = "nc"
                ClassVueAffichage.Affichage(self=True,
                                            texte1="en absence d'indication, le sexe est indiqué nc",
                                            texte2="", texte3="")
                #print("en absence d'indication, le sexe est indiqué nc")

        classement = ClassVueAffichage.Input(self=True, texte1="classement :")
        #classement = input("classement : \n")
        if classement.isdigit():
                ClassVueAffichage.Affichage(self=True,
                                            texte1="classement "+ str(classement) +" ok",
                                            texte2="", texte3="")
                #print("classement ok")
        else:
                classement = 10000
                ClassVueAffichage.Affichage(self=True,
                                            texte1="Error saisie classement, par défaut, "+ str(classement),
                                            texte2="", texte3="")
                #print("Error saisie classement, par défaut, 10000")
        id_joueur = id_libre

        # Serialize l'instance joueurs
        joueur = {"id_joueur": id_joueur, "Nom": nom, "Prenom": prenom, "date de naissance": date_naissance,
                  "sexe": sexe, "Classement": classement}
        ClassJoueurs.CreatJoueurs(self=True,joueur=joueur)
        return(joueur)

def lect_joueurs():# Afficher la liste des joueurs
        #import json

        with open('joueurs.json') as mon_fichier:
                dico = json.load(mon_fichier)

        index = 0
        #faire une fonction qui supprime les {, [, et qui remplace chaque { par un \n
        serialised_joueurs = db_joueurs.all()
        str_joueurs = str(serialised_joueurs)

        print_liste_joueurs=""
        char = "{"
        for x in range(len(char)):
                print_liste_joueurs = str_joueurs.replace(char,"\n")
                print_liste_joueurs = print_liste_joueurs.replace("}", "")
                print_liste_joueurs = print_liste_joueurs.replace(",", "         ")
                print_liste_joueurs = print_liste_joueurs.replace("'", " ")
                #print_liste_joueurs = print_liste_joueurs.replace(":", " ")

        print_liste_joueurs = print_liste_joueurs.replace("[", "")
        print_liste_joueurs = print_liste_joueurs.replace("]", "    ")

        # Appel de la méthode vue du modèle VMC pour affichage de la résultante de la base de données
        ClassVueAffichage.Affichage(self=True,texte1="",texte2="Ci-dessous, la liste des joueurs issus de la base de données :",texte3=print_liste_joueurs + "\n")
        return ()

#supprimer un joueur de la liste pour éventuellement le ressaisir
def sup_joueurs(menu_niv_2):
        with open('joueurs.json') as mon_fichier:
                dico = json.load(mon_fichier)
        #db_joueurs.remove(Todo.Nom == menu_niv_2)
        menu_niv_2=int(menu_niv_2)
        db_joueurs.remove(Todo.id_joueur == menu_niv_2)

#purge de la base de donnée
def purge_joueurs():
        db_joueurs.truncate()