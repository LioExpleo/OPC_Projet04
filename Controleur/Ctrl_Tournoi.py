"""création des joueurs - appel du modele joueur lors de la création des joueurs"""
"""affichage liste joueurs de la base de donnée, suppression d'un joueur de la base de donnée, purge de la base de donnée"""
import os
import re
from Vue.menu import ClassMainMenu
from Modele.Tournoi import ClassTournoi

import json
from tinydb import TinyDB, Query, where
Todo = Query()
db_tournois = TinyDB('tournois.json')

def creat_tournois():
        print ("Creation tournoi tapez \"w\"")
        tournoi = ""
        inst_creat_tournois =""
        inst_creat_tournois = ClassTournoi.CreatTournois(tournoi)

        wd = os.getcwd() #récupération du chemin
        print (wd)
        working_directory = str(wd)
        working_directory_db = working_directory + "/tournois.json"
        mode_ouv_fichier_json = "a+"
        with open('tournois.json', mode_ouv_fichier_json) as fichier_joueur:
                # with open(working_directory_db):
                # print("fichier joueurs.json ouvert en mode \""+ str(mode_ouv_fichier_json) +"\"")
                pass

        # Insertion du joueur saisi dans la base de donnée
        db_tournois.insert(inst_creat_tournois)
        print("affichage db_tounois de contrôleur joueurs")
        print(db_tournois.all())
        return()

def lect_tournois():# Afficher la liste des joueurs
        #import json
        print("Test affichage des joueurs de la base de donnée")
        with open('tournois.json') as mon_fichier:
                dico = json.load(mon_fichier)
        #print("data dico")
        index = 0
        #faire une fonction qui supprime les {, [, et qui remplace chaque { par un \n
        serialised_tournois = db_tournois.all()
        str_tournois = str(serialised_tournois)
        print (str_tournois)
        char = "{"
        for x in range(len(char)):
                print_liste_tournois = str_tournois.replace(char,"\n")
                print_liste_tournois = print_liste_tournois.replace("}", "")
                print_liste_tournois = print_liste_tournois.replace(",", "")

        print_liste_tournois = print_liste_tournois.replace("[", "")
        print_liste_tournois = print_liste_tournois.replace("]", "")

        print("liste des tournois de la base de données :")
        print(print_liste_tournois + "\n")
        return ()

#supprimer un joueur de la liste pour éventuellement le ressaisir
def sup_tournois(menu_niv_2):
        with open('tournois.json') as mon_fichier:
                dico = json.load(mon_fichier)
        db_tournois.remove(Todo.nom == menu_niv_2)

#purge de la base de donnée
def purge_tournois():
        db_tournois.truncate()