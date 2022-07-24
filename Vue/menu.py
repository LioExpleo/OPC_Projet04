import os
import time

class MainMenu():
    def __init__(self, id_tournoi, clavier,niv0,niv1,niv2):
        self.clavier = clavier
        self.niv0 = niv0
        self.niv1 = niv1
        self.niv2 = niv2
        self.id_tournoi =id_tournoi

    def CommandeClavier(self):
        clavier=""
        menu_niv0 = self.niv0
        menu_niv1 = self.niv1
        menu_niv2 = self.niv2
        id_tournoi = self.id_tournoi

        while (clavier != "E"):
            clavier = input("Entrez une commande valide help pour aide ")
            if (clavier != "") and (clavier != "E") :
                if (clavier == "help"):
                    print( "1 pour ..., 2 pour..., 3 pour ..." )

                # MENU TOURNOI
                if (clavier == "1"):
                    menu_niv0 = clavier; menu_niv1= ""; menu_niv2=""
                    print ("TOURNOI : ")
                    print("r pour afficher la liste des tournois - w pour créer un nouveau tournoi, c pour charger un tournoi existant")
                    #print (" Vous avez entré :" + clavier + " TOURNOIS : r pour consultation des tournois, w pour création d'un nouveau tournoi")
                    # si r, requête pour récupération des données d'un tournoi
                    # si w, création d'un tournoi

                #création d'un tournoi
                if (menu_niv0 == "1" and clavier=="w"):
                    menu_niv1 = clavier
                    print ("création de l'instance de classe pour création du tournoi")
                    print("Nom, lieu, date mise en auto, date de fin mise en auto")

                # affiche tous les tournois
                if (menu_niv0 == "1" and clavier=="r"):
                    menu_niv1 = clavier
                    print("requête pour afficher la liste des tournois")

                # charger un tournoi
                if (menu_niv0 == "1" and clavier=="c"):
                    menu_niv1 = clavier
                    print("chargment du tournoi avec son id")

                # MENU JOUEURS
                if (clavier == "2"):
                    menu_niv0 = clavier;menu_niv1 = "";menu_niv2 = ""
                    print("JOUEURS : ")
                    print (" Vous avez entré : " + clavier + " JOUEURS TOURNOIS EN COURS: r pour lecture, w pour création de joueurs, c pour charger")

                    #Si r, requête pour récupération des données des données des joueurs d'un tournoi
                    #21 pour données joueurs 1, 22 pour données joueur 2....
                    # si w, création des joueurs d'un tournoi, touche entrée pour passer au joueur suivant..

                #création de la liste des 8 joueurs
                if (menu_niv0 == "2" and clavier == "w"):
                    menu_niv1 = clavier
                    print ("création de la liste des joueurs, nom, prénom, date de naissance, sexe, classement")
                #if (menu_niv0 == "2" and menu_niv1 == "w" and int(clavier) > 0) and int(clavier) > 9)):

                # affichage la liste des 8 joueurs
                if (menu_niv0 == "2" and clavier == "r"):
                    menu_niv1 = clavier

                # MENU ROUND
                if (clavier == "3"):
                    menu_niv0 = clavier; menu_niv1: ""; menu_niv2: ""
                    print (" Vous avez entré :"+ clavier + " ROUND : AFFICHE LE ROUND EN COURS ET CALCULE LES PAIRES, PUIS LES AFFICHE")

                # MENU MATCH
                if (clavier == "4"):
                    menu_niv0 = clavier; menu_niv1: ""; menu_niv2: ""
                    print (" Vous avez entré :"+ clavier + " MATCH : r pour lecture, w pour écriture; si écriture, "
                        "le round précédant se termine et la saisie des scores est à faire par paire")
                    #chronologiquement, la personne qui saisi doit repasser au 4 pour refaire des round, peut aussi se faire en automatiquement"
                    #si round 4, fin tournoi, mise à jour manuelle du classement des joueurs"

                # MENU REQUETES EN DEHORS DU TOURNOI
                if (clavier == "5"):
                    menu_niv0 = clavier; menu_niv1: ""; menu_niv2: ""
                    print (" Vous avez entré :"+ clavier + " REQUETE CLASSEMENT : r pour lecture, w pour écriture du classement des joueurs en dehors du tournoi ")

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


                if (clavier != 0):
                    #print(clavier)
                    return (id_tournoi,clavier,menu_niv0,menu_niv1,menu_niv2)
        else :
            os._exit(0)

        print ("self.clavier")
        #return self.clavier
        return ("self.clavier")
    #clavier = ""
