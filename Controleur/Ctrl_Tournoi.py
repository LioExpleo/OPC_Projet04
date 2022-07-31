"""création des joueurs - appel du modele joueur lors de la création des joueurs"""
"""affichage liste joueurs de la base de donnée, suppression d'un joueur de la base de donnée, purge de la base de donnée"""
import os
import re
from Vue.menu import ClassMainMenu
from Modele.Tournoi import ClassTournoi
import time
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

#supprimer un tournoi de la liste pour éventuellement le ressaisir
def sup_tournois(menu_niv_2):
        print ("SUPPRESSION D'UN TOURNOI, tapez le nom du tournoi à supprimer, attention 2 tournois pourraient porter le même nom")
        with open('tournois.json') as mon_fichier:
                dico = json.load(mon_fichier)
        db_tournois = TinyDB('tournois.json')
        db_tournois.remove(Todo.nom == menu_niv_2)

#purge de la base de donnée
def purge_tournois():
        db_tournois.truncate()

def select_tournoi():
        print("SELECTION DU TOURNOI")
        id_tournoi_select = ""
        from tinydb import TinyDB, Query, where
        list_tournoi = []
        #Todo = Query()
        db_joueurs = TinyDB('joueurs.json')
        mode_ouv_fichier_json = "r"

        # SELECTION DU TOURNOI
        serialised_tournoi = db_tournois.all()
        str_tournoi = str(serialised_tournoi)
        # print(str_tournoi)

        # faire une fonction qui supprime les {, [, et qui remplace chaque { par un \n
        serialised_joueurs = db_joueurs.all()
        str_joueurs = str(serialised_joueurs)
        # print(str_joueurs)

        char = "{"
        x = 0
        tournoi_cherché = 1
        tournoi_trouvé = 0
        # for x in range(len(str_joueurs)):
        index = 1  # A SUPPRIMER
        for i in serialised_tournoi:
                index = index + 1  # A SUPPRIMER

                # Extraction de l'id
                char = 'id_tournoi'
                PositDebNbre = (str_tournoi.find(char))

                char = "nom"
                PositFinNbre = (str_tournoi.find(char))

                id_tournoi = str_tournoi[(PositDebNbre + 13): (PositFinNbre - 3)]
                print("id tournoi trouvé : " + id_tournoi)
                # Supprimer le 1er tournoi traité de la trame du dictionnaire
                char = '}'
                PositDebNbre = (str_tournoi.find(char))

                str_tournoi = str_tournoi[(PositDebNbre + 2):-1]
                list_tournoi.append(id_tournoi)

                tournoi_cherché = tournoi_cherché + 1

        # print("liste Id tournois")
        # print(list_tournoi)
        str_list_tournoi = str(list_tournoi)
        str_list_tournoi = str_list_tournoi.replace('[', '')
        str_list_tournoi = str_list_tournoi.replace('\',', ' -')
        str_list_tournoi = str_list_tournoi.replace('\']', '')
        str_list_tournoi = str_list_tournoi.replace('\'', 'tournoi n°')
        print("liste des numéros de tournois dans la base de donnée qu'il est possible de sélectionner :")
        print(str_list_tournoi)

        # Faire input de l'id, comparer avec les id de la liste, si id de la liste, mettre
        # dans le tournoi à l'emplacement de l'id 1 au début, et supprimer l'élément de la liste
        # sinon, forcer à ressaisir jusqu'à un id correct
        # if id pas dans la liste, afficher message défaut et recommencer

        tournoi_a_charger = 1
        while (tournoi_a_charger < 2):
                # print("saisie d'un Id de joueur existant pour le joueur n°" + str(joueur_a_charger) + "\n")
                id_a_charger = input("saisie Id ou n° du tournoi existant à sélectionner" + "\n")
                if id_a_charger == "E" or id_a_charger == "e":
                        print("E ou e = commande pour sortir du prog")
                        os._exit(0)

                # Vérification que le tournoi est bien dans la liste des tournois
                if id_a_charger in list_tournoi:
                        tournoi_a_charger = tournoi_a_charger + 1
                        list_tournoi.remove(id_a_charger)
                        time.sleep(0.2)
                        id_tournoi_select = id_a_charger
                        print("Le tournoi " + id_tournoi_select + " est sélectionné")
                        #print("Vous allez pouvoir sélectionner les joueurs dans la base de donnée pour ce tournoi")
                else:
                        print("Ce tournoi n'est pas dans la liste des tournois existants, re-saisir un tournoi de la liste")
        return (id_tournoi_select)

def charge_joueurs_tournoi():
        id_tournoi_select=select_tournoi()
        print ("id_tournoi_select : " + id_tournoi_select)

        from tinydb import TinyDB, Query, where
        list_tournoi = []
        Todo = Query()
        list_joueurs=[]

        db_tournois = TinyDB('tournois.json')
        db_joueurs = TinyDB('joueurs.json')

        mode_ouv_fichier_json = "r"
        #JOUEURS A CHARGER
        with open('joueurs.json') as mon_fichier:
                dico = json.load(mon_fichier)
                # print("data dico")
        index = 0
        # faire une fonction qui supprime les {, [, et qui remplace chaque { par un \n
        serialised_joueurs = db_joueurs.all()
        str_joueurs = str(serialised_joueurs)
        #print(str_joueurs)

        char = "{"
        x=0
        joueur_cherché = 1
        joueur_trouvé = 0
        #for x in range(len(str_joueurs)):
        index=1
        for i in serialised_joueurs:
                #print("index")
                #print(index)
                index = index +1

                #Extraction de l'id
                char = 'id_joueur'
                PositDebNbre = (str_joueurs.find(char))
                #print("PositDebNbre")
                #print(PositDebNbre)

                char = "Nom"
                PositFinNbre = (str_joueurs.find(char))
                #print("PositFinNbre")
                #print(PositFinNbre)

                id_joueur = str_joueurs[(PositDebNbre + 12): (PositFinNbre - 3)]
                #x = txt.split("hello")

                #Supprimer le 1er joueur traité de la trame du dictionnaire
                char = '}'
                PositDebNbre = (str_joueurs.find(char))
                #print("PositDebNbre")
                #print(PositDebNbre)

                str_joueurs=str_joueurs[(PositDebNbre+2):-1]
                #print (str_joueurs)
                #print("id_joueur")
                #print(id_joueur)
                list_joueurs.append(id_joueur)
                joueur_cherché = joueur_cherché + 1
        print("liste Id joueurs")
        print(list_joueurs)
        #Faire input de l'id, comparer avec les id de la liste, si id de la liste, mettre
        #dans le tournoi à l'emplacement de l'id 1 au début, et supprimer l'élément de la liste
        #sinon, forcer à ressaisir jusqu'à un id correct
        # if id pas dans la liste, afficher messsage defaut et recommmencer
        #sinon le charger dans le Tournoi et le supprimer de la liste, puis reproposer la liste pour le prochain joueur à charger
        joueur_a_charger = 1
        while (joueur_a_charger < 9 ):
                #print("saisie d'un Id de joueur existant pour le joueur n°" + str(joueur_a_charger) + "\n")
                id_a_charger = input("saisie Id ou n° de joueur existant pour le joueur n°" + str(joueur_a_charger) + "\n")
                if id_a_charger == "E" or id_a_charger == "e":
                        print("E ou e = commande pour sortir du prog")
                        os._exit(0)
                #print (list_joueurs)
                if id_a_charger in list_joueurs:
                        print("joueur n°"+ id_a_charger + " sélectionné pour le tournoi"+ "\n")
                        list_joueurs.remove(id_a_charger)
                        time.sleep(0.2)
                        str_list_joueurs=str(list_joueurs)
                        str_list_joueurs =str_list_joueurs.replace('[','')
                        str_list_joueurs = str_list_joueurs.replace('\',', ' -')
                        str_list_joueurs = str_list_joueurs.replace('\']', '')
                        str_list_joueurs = str_list_joueurs.replace('\'', 'joueur n°')
                        print ("liste des numéros des joueurs non sélectionnés :")
                        print(str_list_joueurs)
                        print()

                        serialised_tournoi = db_tournois.all()
                        str_tournoi = str(serialised_tournoi)

                        str_tournoi = str(serialised_tournoi)
                        print(str_tournoi)
                        str_id_tournoi_select = str(id_tournoi_select)

                        #Sélection du joueur de la table tournoi à charger
                        id_jx=("id_j"+str(joueur_a_charger))
                        print("id-jx : " + id_jx)
                        print ("id_tournoi_select : " +str(id_tournoi_select))
                        print("id_a_charger : " + str(id_a_charger))
                        print("id_jx : " + str(id_jx))

                        db_tournois = TinyDB('tournois.json')
                        id_tournoi_select=int(id_tournoi_select)
                        db_tournois.update({id_jx: id_a_charger}, Todo.id_tournoi == id_tournoi_select)
                        joueur_a_charger = joueur_a_charger + 1
                else:
                        print("n° de joueur absent de la liste des joueurs ou déjà sélectionné pour le tournoi")