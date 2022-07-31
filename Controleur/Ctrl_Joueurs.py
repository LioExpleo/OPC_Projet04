"""création des joueurs - appel du modele joueur lors de la création des joueurs"""
"""affichage liste joueurs de la base de donnée, suppression d'un joueur de la base de donnée, purge de la base de donnée"""
import os
import re
from Vue.menu import ClassMainMenu
from Modele.Joueurs import ClassJoueurs

import json
from tinydb import TinyDB, Query, where
Todo = Query()
db_joueurs = TinyDB('joueurs.json')

def creat_joueurs():
        print ("Creation joueurs, retapez \"w\" une fois le 1er créé pour retaper le suivant")
        inst_creat_joueurs = ClassJoueurs.CreatJoueurs(self.__class__)

        wd = os.getcwd() #récupération du chemin
        print (wd)
        working_directory = str(wd)
        working_directory_db = working_directory + "/joueurs.json"
        mode_ouv_fichier_json = "a+"
        with open('joueurs.json', mode_ouv_fichier_json) as fichier_joueur:
                # with open(working_directory_db):
                # print("fichier joueurs.json ouvert en mode \""+ str(mode_ouv_fichier_json) +"\"")
                pass

        # Insertion du joueur saisi dans la base de donnée
        db_joueurs.insert(inst_creat_joueurs)
        print("affichage db_joueurs de contrôleur joueurs")
        print(db_joueurs.all())
        return()

def lect_joueurs():# Afficher la liste des joueurs
        #import json

        with open('joueurs.json') as mon_fichier:
                dico = json.load(mon_fichier)
        #print("data dico")
        index = 0
        #faire une fonction qui supprime les {, [, et qui remplace chaque { par un \n
        serialised_joueurs = db_joueurs.all()
        str_joueurs = str(serialised_joueurs)
        #print (str_joueurs)
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

        print()
        print("liste des joueurs de la base de données :")
        print(print_liste_joueurs + "\n")
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
