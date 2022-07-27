"""création du tournoi - appel du modele tournoi afin de creer le tounroi"""
import os
import re
from Vue.menu import ClassMainMenu
from Modele.Joueurs import ClassJoueurs
import json
from Modele.Joueurs import ClassJoueurs
import json

def main_controleur_joueurs():
        saisie_clavier =""
        menu_niv_0 = ""
        menu_niv_1 = ""
        menu_niv_2 = ""
        derniere_saisie=""

        while (saisie_clavier!="E"):
                #Lancer la méthode CommandeClavier de la classe MainMenu
                id_tournoi,saisie_clavier, menu_niv_0, menu_niv_1, menu_niv_2 = ClassMainMenu(id_tournoi="", clavier="",niv0=menu_niv_0,niv1=menu_niv_1,niv2=menu_niv_2 ).CommandeClavier()
                print ("return menu niv0 : "+ menu_niv_0)
                print("return menu niv1 : " + menu_niv_1)
                print("return menu niv2 : " + menu_niv_2)
                print("return id_tournoi : " + id_tournoi)

                from tinydb import TinyDB, Query, where
                Todo = Query()
                # Création de la base de donnée db_joueurs
                db_joueurs = TinyDB('joueurs.json')

                #Ajouter des joueurs
                if (menu_niv_0 == "J" and menu_niv_1 =="w"):
                        print ("Creation joueurs, retapez \"w\" une fois le 1er créé pour retaper le suivant")
                        joueur = ""
                        inst_creat_joueurs = ClassJoueurs.CreatJoueurs(joueur)

                        # Ecrire dans le fichier json fichier_joueur le contenu de joueur
                        #with open('joueurs.json', 'w') as fichier_joueur:
                        #        json.dump(inst_creat_joueurs, fichier_joueur)

                        #CREATION DE LA TABLE DB JOUEURS
                        # TinyDB - Représente ta base de donnée
                        # Query - Permet d'interroger ta base de donnée
                        # where - Permet d'affiner tes critères de recherche
                        ####################from tinydb import TinyDB, Query, where
                        ####################Todo = Query()

                        # Recherche répertoire courant
                        wd = os.getcwd()

                        # *************** verif si fichier existe
                        working_directory = str(wd)
                        working_directory_db = working_directory + "/joueurs.json"
                        mode_ouv_fichier_json = "a+"
                        try:
                               with open('joueurs.json', mode_ouv_fichier_json) as fichier_joueur:
                               #with open(working_directory_db):
                                       print("fichier joueurs.json ouvert en mode \""+ str(mode_ouv_fichier_json) +"\"")
                                       pass
                        except IOError:
                               print("Erreur! Le fichier n a pas pu être ouvert")
                        # *********************************************************

                        # Création de la base de donnée db_joueurs
                        #db_joueurs = TinyDB('joueurs.json')

                        # Insertion du joueur saisi dans la base de donnée
                        db_joueurs.insert(inst_creat_joueurs)
                        #db_joueurs.insert(inst_creat_joueurs)

                        print("fichier_joueur")
                        print(fichier_joueur)
                        print("db_joueurs")
                        print(db_joueurs.all())

                # Afficher la liste des joueurs
                if (menu_niv_0 == "J" and menu_niv_1 == "r"):
                        #import json
                        with open('joueurs.json') as mon_fichier:
                                dico = json.load(mon_fichier)
                        #print("data dico")
                        index = 0
                        #faire une fonction qui supprime les {, [, et qui remplace chaque { par un \n
                        serialised_joueurs = db_joueurs.all()
                        str_joueurs = str(serialised_joueurs)
                        print (str_joueurs)
                        char = "{"
                        for x in range(len(char)):
                                print_liste_joueurs = str_joueurs.replace(char,"\n")
                                print_liste_joueurs = print_liste_joueurs.replace("}", "")
                                print_liste_joueurs = print_liste_joueurs.replace(",", "")

                        print_liste_joueurs = print_liste_joueurs.replace("[", "")
                        print_liste_joueurs = print_liste_joueurs.replace("]", "")

                        print("liste des joueurs de la base de données :")
                        print(print_liste_joueurs + "\n")

                        '''
                        while (index >= 0):
                                index = index + 1
                                str_index = str(index)
                                try:
                                        nom_dico = (dico["_default"][str_index])  # [""]
                                        print("dico, joueur : " + str_index)
                                        print(nom_dico)
                                except KeyError:
                                        index = index - 1
                                        print()
                                        print("fin de la liste des " + str(index) + " joueurs\n")
                                        break

                        print(db_joueurs.search(Todo.nom != 'f'))
                        #[{'count': 3, 'type': 'peach'}]
                        #>> > db.search(Fruit.count > 5)
                        #[{'count': 7, 'type': 'apple'}]




                        #Reboucler à l'infini, quand "except KeyError", la liste est terminée
                        while (index >= 0):
                                index = index +1
                                str_index = str(index)
                                try :
                                        nom_dico = (dico["_default"][str_index])  # [""]
                                        print("dico, joueur : " + str_index)
                                        print(nom_dico)
                                except KeyError:
                                        index=index-1
                                        print()
                                        print("fin de la liste des " + str(index) + " joueurs\n")
                                        break
                        
                                De la même manière, vous pouvez également supprimer des documents:

                                >>> db.remove(Fruit.count < 5)
                                >>> db.all()
                                [{'count': 10, 'type': 'apple'}]
                                
                                Vous pouvez également itérer sur les documents stockés :

                                >>> for item in db:
                                >>>     print(item)
                                {'count': 7, 'type': 'apple'}
                                {'count': 3, 'type': 'peach'}
                                Bien sûr, vous voudrez également rechercher des documents spécifiques. Essayons:
                                >>> Fruit = Query()
                                >>> db.search(Fruit.type == 'peach')
                                [{'count': 3, 'type': 'peach'}]
                                >>> db.search(Fruit.count > 5)
                                [{'count': 7, 'type': 'apple'}]
                                
                                Ensuite, nous allons mettre à jour le champ des pommes:count
                                >>> db.update({'count': 10}, Fruit.type == 'apple')
                                >>> db.all()
                                [{'count': 10, 'type': 'apple'}, {'count': 3, 'type': 'peach'}]
                                           
                        '''
                        #print(db_joueurs.all())

                #supprimer un joueur de la liste pour éventuellement le ressaisir
                if (menu_niv_0 == "J" and menu_niv_1 == "sup" and menu_niv_2 !=""):
                        #int_menu_niv_2 = int(menu_niv_2)
                        #print("int_menu_niv_2")
                        #print (int_menu_niv_2 )
                        with open('joueurs.json') as mon_fichier:
                                dico = json.load(mon_fichier)
                        db_joueurs.remove(Todo.nom == menu_niv_2)

                #purge de la base de donnée
                if (menu_niv_0 == "J" and menu_niv_1 == "purge" and menu_niv_2 == "o"):
                        # purge de la table
                        db_joueurs.truncate()

        return(menu_niv_0,menu_niv_1,menu_niv_2,id_tournoi)

'''
        print("TOURNOI : ")
        print("r pour afficher la liste des tournois - w pour créer un nouveau tournoi, c pour charger un tournoi existant")

        # création d'un tournoi
        if (menu_niv0 == "1" and clavier == "w"):
                menu_niv1 = clavier
                print("création de l'instance de classe pour création du tournoi")
                # Echange avec le contrôleur qui créé l'instance de tournoi à partir du modèle
                # L'échange

                print("Nom, lieu, date mise en auto, date de fin mise en auto")

        # affiche tous les tournois
        if (menu_niv0 == "1" and clavier == "r"):
                menu_niv1 = clavier
                print("requête pour afficher la liste des tournois")

        # charger un tournoi
        if (menu_niv0 == "1" and clavier == "c"):
                menu_niv1 = clavier
                print("chargment du tournoi avec son id")

        # MENU JOUEURS
        if (clavier == "2"):
                menu_niv0 = clavier;
                menu_niv1 = "";
                menu_niv2 = ""
                print("JOUEURS : ")
                print(" Vous avez entré : " + clavier + " JOUEURS TOURNOIS EN COURS: r pour lecture, w pour création de joueurs, c pour charger")

                # Si r, requête pour récupération des données des données des joueurs d'un tournoi
                # 21 pour données joueurs 1, 22 pour données joueur 2....
                # si w, création des joueurs d'un tournoi, touche entrée pour passer au joueur suivant..

        # création de la liste des 8 joueurs
        if (menu_niv0 == "2" and clavier == "w"):
                menu_niv1 = clavier
                print("création de la liste des joueurs, nom, prénom, date de naissance, sexe, classement")
        # if (menu_niv0 == "2" and menu_niv1 == "w" and int(clavier) > 0) and int(clavier) > 9)):

        # affichage la liste des 8 joueurs
        if (menu_niv0 == "2" and clavier == "r"):
                menu_niv1 = clavier

        # MENU ROUND
        if (clavier == "3"):
                menu_niv0 = clavier;
                menu_niv1: "";
                menu_niv2: ""
                print(" Vous avez entré :" + clavier + " ROUND : AFFICHE LE ROUND EN COURS ET CALCULE LES PAIRES, PUIS LES AFFICHE")

        # MENU MATCH
        if (clavier == "4"):
                menu_niv0 = clavier;
                menu_niv1: "";
                menu_niv2: ""
                print(" Vous avez entré :" + clavier + " MATCH : r pour lecture, w pour écriture; si écriture, "
                                                       "le round précédant se termine et la saisie des scores est à faire par paire")
                # chronologiquement, la personne qui saisi doit repasser au 4 pour refaire des round, peut aussi se faire en automatiquement"
                # si round 4, fin tournoi, mise à jour manuelle du classement des joueurs"

        # MENU REQUETES EN DEHORS DU TOURNOI
        if (clavier == "5"):
                menu_niv0 = clavier;
                menu_niv1: "";
                menu_niv2: ""
                print(" Vous avez entré :" + clavier + " REQUETE CLASSEMENT : r pour lecture, w pour écriture du classement des joueurs en dehors du tournoi ")

        if (clavier == "10"):
                menu_niv0 = clavier
                print(" Vous avez entré :" + clavier + " REQUETE RAPPORT alphab acteurs: liste de tous les acteurs par ordre alphabétique")

        if (clavier == "11"):
                menu_niv0 = clavier
                print(" Vous avez entré :" + clavier + " REQUETE  RAPPORT classement acteurs : liste de tous les acteurs par classement")

        if (clavier == "12"):
                menu_niv0 = clavier
                print(" Vous avez entré :" + clavier + " REQUETE RAPPORT Tournois : liste de tous les tournois")

        if (clavier == "13"):
                menu_niv0 = clavier
                print(" Vous avez entré :" + clavier + " REQUETE Rapport tours Tournois : Entrez l'ID du tournoi pour afficher les tours du tournoi,"
                                                       " liste des tournois avec la commande 1, et r")

        if (clavier == "14"):
                menu_niv0 = clavier
                print(" Vous avez entré :" + clavier + " REQUETE Tournois : Entrez l'ID du tournoi pour afficher les résultats des matchs *Affiche paires et score*")

        if (clavier == "15"):
                menu_niv0 = clavier
                print(" Vous avez entré :" + clavier + " REQUETE Rapport : Entrez l'ID du tournoi pour avoir la liste de tous les joueurs d'un tournoi par ordre alphabétique")
                print(" Vous avez entré :" + clavier + " REQUETE requête vers base de données  : liste de tous les joueurs d'un tournoi par ordre alphabétique")

        if (clavier == "16"):
                menu_niv0 = clavier
                print(" Vous avez entré :" + clavier + " REQUETE Rapport : Entrez l'ID du tournoi pour avoir la liste de tous les joueurs d'un tournoi par ordre alphabétique")
                print(" Vous avez entré :" + clavier + " REQUETE requête vers base de données : liste de tous les joueurs d'un tournoi par classement")
'''