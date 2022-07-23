import os
import time

class MainMenu():
    def __init__(self, clavier):
        self.clavier = clavier

    def CommandeClavier(self):
        clavier=""
        while (clavier != "E"):
            clavier = input("Entrez une commande valide help pour aide ")
            if (clavier != "") and (clavier != "E") :
                if (clavier == "help"):
                    print( "1 pour ..., 2 pour..., 3 pour ..." )

                if (clavier == "1"):
                    print ("TOURNOI")
                    #print (" Vous avez entré :" + clavier + " TOURNOIS : r pour consultation des tournois, w pour création d'un nouveau tournoi")
                    # si r, requête pour récupération des données d'un tournoi
                    # si w, création d'un tournoi

                if (clavier == "2"):
                    print (" Vous avez entré :" + clavier + " JOUEURS TOURNOIS EN COURS: r pour lecture, w pour création de joueurs")
                    # si r, requête pour récupération des données des données des joueurs d'un tournoi
                    #21 pour données joueurs 1, 22 pour données joueur 2....
                    # si w, création des joueurs d'un tournoi, touche entrée pour passer au joueur suivant..

                if (clavier == "3"):
                    print (" Vous avez entré :"+ clavier + " ROUND : AFFICHE LE ROUND EN COURS ET CALCULE LES PAIRES, PUIS LES AFFICHE")

                if (clavier == "4"):
                    print (" Vous avez entré :"+ clavier + " MATCH : r pour lecture, w pour écriture; si écriture, "
                        "le round précédant se termine et la saisie des scores est à faire par paire")
                    #chronologiquement, la personne qui saisi doit repasser au 4 pour refaire des round, peut aussi se faire en automatiquement"
                    #si round 4, fin tournoi, mise à jour manuelle du classement des joueurs"

                if (clavier == "5"):
                    print (" Vous avez entré :"+ clavier + " REQUETE CLASSEMENT : r pour lecture, w pour écriture du classement des joueurs en dehors du tournoi ")

                if (clavier == "10"):
                    print(" Vous avez entré :" + clavier + " REQUETE RAPPORT alphab acteurs: liste de tous les acteurs par ordre alphabétique")

                if (clavier == "11"):
                    print(" Vous avez entré :" + clavier + " REQUETE  RAPPORT classement acteurs : liste de tous les acteurs par classement")

                if (clavier == "12"):
                    print(" Vous avez entré :" + clavier + " REQUETE RAPPORT Tournois : liste de tous les tournois")

                if (clavier == "13"):
                    print(" Vous avez entré :" + clavier + " REQUETE Rapport tours Tournois : Entrez l'ID du tournoi pour afficher les tours du tournoi,"
                                                           " liste des tournois avec la commande 1, et r")

                if (clavier == "14"):
                    print(" Vous avez entré :" + clavier + " REQUETE Tournois : Entrez l'ID du tournoi pour afficher les résultats des matchs *Affiche paires et score*")

                if (clavier == "15"):
                    print(" Vous avez entré :" + clavier + " REQUETE Rapport : Entrez l'ID du tournoi pour avoir la liste de tous les joueurs d'un tournoi par ordre alphabétique")
                    print(" Vous avez entré :" + clavier + " REQUETE requête vers base de données  : liste de tous les joueurs d'un tournoi par ordre alphabétique")

                if (clavier == "16"):
                    print(" Vous avez entré :" + clavier + " REQUETE Rapport : Entrez l'ID du tournoi pour avoir la liste de tous les joueurs d'un tournoi par ordre alphabétique")
                    print(" Vous avez entré :" + clavier + " REQUETE requête vers base de données : liste de tous les joueurs d'un tournoi par classement")

                if (clavier != 0):
                    #print(clavier)
                    return (clavier)
        else :
            os._exit(0)

        print ("self.clavier")
        #return self.clavier
        return ("self.clavier")
    #clavier = ""
