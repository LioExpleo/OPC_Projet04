import os
import time

from Modele.Joueurs import ClassJoueurs
#from Controleur.Contrôleur_Tournoi import ClassControleurTournoi
#from Controleur.Test_Contrôleur_Joueurs import creat_joueurs
#from Controleur.Contrôleur_Joueurs import main_controleur_joueurs

class ClassMainMenu():
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
                if (clavier == "T"):
                    menu_niv0 = clavier; menu_niv1= ""; menu_niv2=""
                    print ("TOURNOI : ")
                    print("r pour afficher la liste des tournois - w pour créer un nouveau tournoi, c pour charger un tournoi existant")
                    #ClassControleurTournoi()
                    #print (" Vous avez entré :" + clavier + " TOURNOIS : r pour consultation des tournois, w pour création d'un nouveau tournoi")
                    # si r, requête pour récupération des données d'un tournoi
                    # si w, création d'un tournoi

                #création d'un tournoi
                if (menu_niv0 == "T" and clavier=="w"):
                    menu_niv0 = "T"
                    menu_niv1 = clavier
                    print ("création de l'instance de classe pour création du tournoi")
                    #Echange avec le contrôleur qui créé l'instance de tournoi à partir du modèle
                    print("Nom, lieu, date mise en auto, date de fin mise en auto")
                    tournoi=""
                    #InstCreatTournoi = ClassControleurTournoi(tournoi).main_controleur_tournoi()
                # affiche tous les tournois
                if (menu_niv0 == "T" and clavier=="r"):
                    menu_niv1 = clavier
                    print("requête pour afficher la liste des tournois")
                    #main_controleur_tournoi()
                #*******************************
                # possibilité de purger la table, utile pour debug
                if (menu_niv0 == "T" and clavier == "purge"):
                    menu_niv1 = clavier
                    print("vous allez purger la base de donnée des tournois tapez :\"o\" pour confirmer")
                if (menu_niv0 == "T" and menu_niv1 == "purge" and clavier == "o"):
                    menu_niv2 = clavier
                    #main_controleur_tournoi()

                # possibilité d'effacer un joueur de la liste si erreur de saisie
                if (menu_niv0 == "T" and clavier == "sup"):
                    menu_niv1 = clavier
                    print(
                        "vous voulez supprimer un tournoi, suite à une erreur de saisie par exemple, de la liste des tournois, tapez le nom du tournoi pour le supprimer !")
                    print(
                        "Attention tous les tournois portant ce nom seront supprimés, mais le cahier des charges ne prévoyait pas de pouvoir supprimer des tournois,")
                    print(
                        "donc noter les caractéristiques de tous les tounrois portant ce nom pour éventuellement les ressaisir.")

                if (menu_niv0 == "T" and menu_niv1 == "sup" and clavier != "sup"):
                    menu_niv2 = clavier
                    #main_controleur_tournoi()

                # charger un tournoi
                if (menu_niv0 == "T" and clavier=="c"):
                    menu_niv1 = clavier
                    print("chargment du tournoi avec son id")

                # ***************************************************************************************************************************
                # ***************************************************************************************************************************
                # MENU JOUEURS
                if (clavier == "J"):
                    menu_niv0 = clavier;menu_niv1 = "";menu_niv2 = ""
                    print("JOUEURS : ")
                    print (" Vous avez entré : " + clavier + " JOUEURS TOURNOIS EN COURS: r pour lecture, w pour création de joueurs, c pour charger")
                    #main_controleur_joueurs()
                    #Si r, requête pour récupération des données des données des joueurs d'un tournoi
                    #21 pour données joueurs 1, 22 pour données joueur 2....
                    # si w, création des joueurs d'un tournoi, touche entrée pour passer au joueur suivant..

                #création de la liste des joueurs
                if (menu_niv0 == "J" and clavier == "w"):
                    menu_niv1 = clavier
                    print ("création de la liste des joueurs, nom, prénom, date de naissance, sexe, classement")

                # affichage la liste des joueurs pour les sélectionner ensuite dans le tournoi
                if (menu_niv0 == "J" and clavier == "r"):
                    menu_niv1 = clavier


                # possibilité de purger la table, utile pour debug
                if (menu_niv0 == "J" and clavier == "purge"):
                    menu_niv1 = clavier
                    print("vous allez purger la base de donnée des joueurs tapez :\"o\" pour confirmer")

                if (menu_niv0 == "J" and menu_niv1 == "purge" and clavier == "o"):
                    menu_niv2 = clavier


                # possibilité d'effacer un joueur de la liste si erreur de saisie
                if (menu_niv0 == "J" and clavier == "sup"):
                    menu_niv1 = clavier
                    print("vous voulez supprimer un joueur, suite à une erreur de saisie par exemple, de la liste des joueurs, tapez le nom du joueur pour le supprimer !")
                    print("Attention tous les joueurs portant ce nom seront supprimés, mais le cahier des charges ne prévoyait pas de pouvoir supprimer des joueurs,")
                    print("donc noter les caractéristiques de tous les joueurs portant ce nom pour éventuellement les ressaisir.")


                if (menu_niv0 == "J" and menu_niv1 == "sup" and clavier!="sup"):
                    menu_niv2 = clavier

                #****************************************************************
                # MENU ROUND
                if (clavier == "R"):
                    menu_niv0 = clavier; menu_niv1: ""; menu_niv2: ""
                    print (" Vous avez entré :"+ clavier + " ROUND : AFFICHE LE ROUND EN COURS ET CALCULE LES PAIRES, PUIS LES AFFICHE")

                # MENU MATCH
                if (clavier == "M"):
                    menu_niv0 = clavier; menu_niv1: ""; menu_niv2: ""
                    print (" Vous avez entré :"+ clavier + " MATCH : r pour lecture, w pour écriture; si écriture, "
                        "le round précédant se termine et la saisie des scores est à faire par paire")
                    #chronologiquement, la personne qui saisi doit repasser au 4 pour refaire des round, peut aussi se faire en automatiquement"
                    #si round 4, fin tournoi, mise à jour manuelle du classement des joueurs"

                # MENU REQUETES EN DEHORS DU TOURNOI
                if (clavier == "C"):
                    menu_niv0 = clavier; menu_niv1: ""; menu_niv2: ""
                    print (" Vous avez entré :"+ clavier + " REQUETE CLASSEMENT : r pour lecture, w pour écriture du classement des joueurs en dehors du tournoi ")

                if (clavier == "R1"):
                    menu_niv0 = clavier
                    print(" Vous avez entré :" + clavier + " REQUETE RAPPORT alphab acteurs: liste de tous les acteurs par ordre alphabétique")

                if (clavier == "R2"):
                    menu_niv0 = clavier
                    print(" Vous avez entré :" + clavier + " REQUETE  RAPPORT classement acteurs : liste de tous les acteurs par classement")

                if (clavier == "R3"):
                    menu_niv0 = clavier
                    print(" Vous avez entré :" + clavier + " REQUETE RAPPORT Tournois : liste de tous les tournois")

                if (clavier == "R4"):
                    menu_niv0 = clavier
                    print(" Vous avez entré :" + clavier + " REQUETE Rapport tours Tournois : Entrez l'ID du tournoi pour afficher les tours du tournoi,"
                                                           " liste des tournois avec la commande 1, et r")
                if (clavier == "R5"):
                    menu_niv0 = clavier
                    print(" Vous avez entré :" + clavier + " REQUETE Tournois : Entrez l'ID du tournoi pour afficher les résultats des matchs *Affiche paires et score*")

                if (clavier == "R6"):
                    menu_niv0 = clavier
                    print(" Vous avez entré :" + clavier + " REQUETE Rapport : Entrez l'ID du tournoi pour avoir la liste de tous les joueurs d'un tournoi par ordre alphabétique")
                    print(" Vous avez entré :" + clavier + " REQUETE requête vers base de données  : liste de tous les joueurs d'un tournoi par ordre alphabétique")

                if (clavier == "R7"):
                    menu_niv0 = clavier
                    print(" Vous avez entré :" + clavier + " REQUETE Rapport : Entrez l'ID du tournoi pour avoir la liste de tous les joueurs d'un tournoi par ordre alphabétique")
                    print(" Vous avez entré :" + clavier + " REQUETE requête vers base de données : liste de tous les joueurs d'un tournoi par classement")


                if (clavier != 0):
                    #print(clavier)
                    return (id_tournoi,clavier,menu_niv0,menu_niv1,menu_niv2)
        else :
            print("os.exit")
            os._exit(0)

        print ("self.clavier")
        return (id_tournoi,clavier,menu_niv0,menu_niv1,menu_niv2)
