import os
#Appel du prog qui gère les différents menus du programme
#Import à partir de directory -Vue- et du prog -menu- de la classe -MainMenu-
from Vue.menu import MainMenu
#Import à partir de directory -Modele- et du prog -Tournoi- de la classe -Tournoi-
from Modele.Tournoi import Tournoi


saisie_clavier =""
derniere_saisie=""

while (saisie_clavier!="E"):
    #Lancer la méthode CommandeClavier de la classe MainMenu
    saisie_clavier=MainMenu(clavier="").CommandeClavier()
    #print ("récupération de la valeur entrée au clavier : " + saisie_clavier )

    # Création ou affichage de la liste des tournois
    if saisie_clavier == "1":
        print ("appel de la méthode de la classe pour créer ou afficher la liste des tournois")
        print("r pour afficher la liste des tournois - w pour créer un nouveau tournoi")

    if (derniere_saisie== "1" and saisie_clavier == "r"):
        print("appel de la méthode de la classe pour afficher la liste des tournois")

    if (derniere_saisie == "1" and saisie_clavier == "w"):
        print("appel de la méthode de la classe pour créer un nouveau tournoi")

        #tournoi = créer_tournoi()

    if saisie_clavier == "2":
        print ("appel de la méthode de la classe pour créer les joueurs")
        #joueurs = créer_joueurs()

    derniere_saisie = saisie_clavier


else:
    os._exit(0)