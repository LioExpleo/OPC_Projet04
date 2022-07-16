import os
import time

clavier =""

while (clavier != "E"):
    clavier = input("Entrez une commande ")
    if (clavier != "") and (clavier != "E") :
        Err_saisie = True
        if (clavier == "1"):
            print (" Vous avez entré :" + clavier + " TOURNOIS EN COURS: r pour lecture, w pour écriture")
            Err_saisie = False

        if (clavier == "2"):
            print (" Vous avez entré :" + clavier + " JOUEURS TOURNOIS EN COURS: r pour lecture, w pour écriture")
            Err_saisie = False

        if (clavier == "3"):
            print (" Vous avez entré :"+ clavier + " ROUND : CALCULE ET AFFICHE ROUND EN COURS")
            Err_saisie = False

        if (clavier == "4"):
            print (" Vous avez entré :"+ clavier + " MATCH : r pour lecture, w pour écriture; si écriture, le round précédant se termine")
            Err_saisie = False
            #chronologiquement, la personne qui saisi doit repasser au 4 pour refaire des round, peut aussi se faire en automatiquement"
            #si round 4, fin tournoi, mise à jour manuelle du classement des joueurs"

        if (clavier == "5"):
            print (" Vous avez entré :"+ clavier + " REQUETE CLASSEMENT : r pour lecture, w pour écriture du classement des joueurs en dehors du tournoi ")
            Err_saisie = False

        if (clavier == "10"):
            print(" Vous avez entré :" + clavier + " REQUETE RAPPORT alphab acteurs: liste de tous les acteurs par ordre alphabétique")
        Err_saisie = False

        if (clavier == "11"):
            print(" Vous avez entré :" + clavier + " REQUETE  RAPPORT classement acteurs : liste de tous les acteurs par classement")
        Err_saisie = False

        if (clavier == "12"):
            print(" Vous avez entré :" + clavier + " REQUETE RAPPORT Tournois : liste de tous les tournois")
        Err_saisie = False

        if (clavier == "13"):
            print(" Vous avez entré :" + clavier + " REQUETE Rapport tours Tournois : Entrez l'ID du tournoi pour afficher les tours du tournoi")
            #print(" Vous avez entré :" + clavier + " ")
        Err_saisie = False

        if (clavier == "14"):
            print(" Vous avez entré :" + clavier + " REQUETE Tournois : Entrez l'ID du tournoi pour afficher les résultats des matchs *Affiche paires et score*")
        Err_saisie = False

        if (clavier == "15"):
            print(" Vous avez entré :" + clavier + " REQUETE Rapport : Entrez l'ID du tournoi pour avoir la liste de tous les joueurs d'un tournoi par ordre alphabétique")
            print(" Vous avez entré :" + clavier + " REQUETE requête vers base de données  : liste de tous les joueurs d'un tournoi par ordre alphabétique")
        Err_saisie = False

        if (clavier == "16"):
            print(" Vous avez entré :" + clavier + " REQUETE Rapport : Entrez l'ID du tournoi pour avoir la liste de tous les joueurs d'un tournoi par ordre alphabétique")
            print(" Vous avez entré :" + clavier + " REQUETE requête vers base de données : liste de tous les joueurs d'un tournoi par classement")
        Err_saisie = False

        if (Err_saisie == True):
            print ("commande <" + clavier + "> inconnue")

else :
    os._exit(0)
clavier = ""
