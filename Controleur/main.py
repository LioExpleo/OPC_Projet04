"""création du tournoi - appel du modele tournoi afin de creer le tounroi"""

from Vue.menu import ClassMainMenu
from Modele.Joueurs import ClassJoueurs
import json

def main_controleur():
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

                if (menu_niv_0 == "2" and menu_niv_1 =="w"):
                        print ("Creation joueurs")
                        poubelle = ""
                        inst_creat_joueurs = ClassJoueurs.CreatJoueurs(poubelle)
                        # Ecrire dans le fichier json fichier_joueur le contenu de joueur
                        with open('joueurs.json', 'w') as fichier_joueur:
                                json.dump(inst_creat_joueurs, fichier_joueur)

                        print("fichier_joueur")
                        print(fichier_joueur)


                        #CreatJoueurs()

        return(menu_niv_0,menu_niv_1,menu_niv_2,id_tournoi)



#faire un programme qui prend en paramètre ou attribut (menu_niv_0,menu_niv_1,menu_niv_2,id_tournoi)
#et lance une commande en sortie

#si niv0 = 1 et w, creation de l'instance de classe pour écrire un tournoi - commande "write_tournoi"
#si niv0 = 1 et l, creation de l'instance de classe pour afficher la liste des tournois - commande "requête_tournoi"
#si niv0 = 1 et c, creation de l'instance de classe pour charger un tournoi - commande

#si niv0 = 2 et w, creation de l'instance de classe pour écrire les 8 joueurs dans la base de donnée - commande "write_joueurs"
#si niv0 = 3 et l, creation de l'instance de classe pour lire les joueurs du tournoi - commande "Requete_joueurs"

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