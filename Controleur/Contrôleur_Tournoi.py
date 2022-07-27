"""création du tournoi - appel du modele tournoi afin de creer le tounroi"""
import os
import re
#from Vue.menu import ClassMainMenu
from Modele.Tournoi import ClassTournoi
import json

class ClassControleurTournoi:
    def __init__(self,tournoi):
            self.tournoi=tournoi

    def main_controleur_tournoi(self):
        saisie_clavier =""
        menu_niv_0 = ""
        menu_niv_1 = ""
        menu_niv_2 = ""
        saisie_clavier =""

        while (saisie_clavier!="E"):
                print("Appel main controleur tournoiiiiiiiiiiiiiiiii")
                #Lancer la méthode CommandeClavier de la classe MainMenu
                id_tournoi,saisie_clavier, menu_niv_0, menu_niv_1, menu_niv_2 = ClassMainMenu(id_tournoi="", clavier="",niv0=menu_niv_0,niv1=menu_niv_1,niv2=menu_niv_2 ).CommandeClavier()
                print ("return menu niv0 : "+ menu_niv_0)
                print("return menu niv1 : " + menu_niv_1)
                print("return menu niv2 : " + menu_niv_2)
                print("return id_tournoi : " + id_tournoi)

                from tinydb import TinyDB, Query, where
                Todo = Query()
                # Création de la base de donnée db_joueurs
                db_tournois = TinyDB('tournois.json')

                #Ajouter des joueurs
                if (menu_niv_0 == "T" and menu_niv_1 =="w"):
                        print ("Creation tournoi, retapez \"w\" tapez w pour création")
                        tournoi = ""
                        inst_creat_tournoi = ClassTournoi.CreatTournois(tournoi)

                        # Recherche répertoire courant
                        wd = os.getcwd()

                        # *************** verif si fichier existe
                        working_directory = str(wd)
                        working_directory_db = working_directory + "/tournoi.json"
                        mode_ouv_fichier_json = "a+"
                        try:
                               with open('joueurs.json', mode_ouv_fichier_json) as fichier_joueur:
                               #with open(working_directory_db):
                                       #print("fichier joueurs.json ouvert en mode \""+ str(mode_ouv_fichier_json) +"\"")
                                       pass
                        except IOError:
                               print("Erreur! Le fichier n a pas pu être ouvert")
                        # *********************************************************

                        # Création de la base de donnée db_joueurs
                        #db_joueurs = TinyDB('joueurs.json')

                        # Insertion du joueur saisi dans la base de donnée
                        db_tournois.insert(inst_creat_tournoi)

                        print("affichage db_tournois de contrôleur tournois")
                        print(db_tournois.all())

                # Afficher la liste des tournois
                if (menu_niv_0 == "T" and menu_niv_1 == "r"):
                        #import json
                        with open('tournois.json') as mon_fichier:
                                dico = json.load(mon_fichier)
                        #print("data dico")
                        index = 0
                        #faire une fonction qui supprime les {, [, et qui remplace chaque { par un \n
                        serialised_tournois = db_tournois.all()
                        str_tournois = str(serialised_tournois)

                        #print (str_tournois)
                        char = "{"
                        for x in range(len(char)):
                                print_liste_tournois = str_tournois.replace(char,"\n")
                                print_liste_tournois = print_liste_tournois.replace("}", "")
                                print_liste_tournois = print_liste_tournois.replace(",", "")

                        print_liste_tournois = print_liste_tournois.replace("[", "")
                        print_liste_tournois = print_liste_tournois.replace("]", "")

                        print ()
                        print("liste des tournois de la base de données :")
                        print(print_liste_tournois + "\n")

                #supprimer un tournoi de la liste pour éventuellement le ressaisir
                if (menu_niv_0 == "T" and menu_niv_1 == "sup" and menu_niv_2 !=""):
                        with open('tournois.json') as mon_fichier:
                                dico = json.load(mon_fichier)
                        db_tournois.remove(Todo.nom == menu_niv_2)

                #purge de la base de donnée
                if (menu_niv_0 == "T" and menu_niv_1 == "purge" and menu_niv_2 == "o"):
                        db_joueurs.truncate()

        return()
