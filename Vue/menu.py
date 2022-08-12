import os

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

        # *********************************** Exit prog *********************************
        while (clavier != "E"):
            clavier = input("Entrez une commande valide help pour aide ")
            if (clavier != "") and (clavier != "E") :
                if (clavier == "help"):
                    print( "1 pour ..., 2 pour..., 3 pour ..." )

                # *********************************** MENU TOURNOI *********************************
                if (clavier == "T"):
                    menu_niv0 = clavier; menu_niv1= ""; menu_niv2=""
                    print ("TOURNOI : ")
                    print("r pour afficher la liste des tournois - w pour créer un nouveau tournoi, c pour charger les joueurs dans un tournoi existant")

                #création d'un tournoi
                if (menu_niv0 == "T" and clavier=="w"):
                    menu_niv0 = "T"
                    menu_niv1 = clavier
                    print ("création de l'instance de classe pour création du tournoi")
                    #Echange avec le contrôleur qui créé l'instance de tournoi à partir du modèle
                    print("Nom, lieu, date mise en auto, date de fin mise en auto")
                    tournoi=""

                #affichage se tous les tournois
                if (menu_niv0 == "T" and clavier=="r"):
                    menu_niv1 = clavier
                    print("requête pour afficher la liste des tournois")

                #purge de la table des tournois, utile pour debug
                if (menu_niv0 == "T" and clavier == "purge"):
                    menu_niv1 = clavier
                    print("vous allez purger la base de donnée des tournois tapez :\"o\" pour confirmer")
                if (menu_niv0 == "T" and menu_niv1 == "purge" and clavier == "o"):
                    menu_niv2 = clavier

                #effacement d'un joueur de la liste si erreur de saisie
                if (menu_niv0 == "T" and clavier == "sup"):
                    menu_niv1 = clavier
                    print(
                        "vous voulez supprimer un tournoi, suite à une erreur de saisie par exemple, de la liste des tournois, tapez l'identifiant du tournoi pour le supprimer !")
                #suppression d'un tournoi
                if (menu_niv0 == "T" and menu_niv1 == "sup" and clavier != "sup"):
                    menu_niv2 = clavier

                # sélectionner du tournoi et chargement des joueurs dans le tournoi
                if (menu_niv0 == "T" and clavier=="c"):
                    menu_niv1 = clavier
                    print("chargement du tournoi avec son id")


                #************************************MENU JOUEURS *********************************
                if (clavier == "J"):
                    menu_niv0 = clavier;menu_niv1 = "";menu_niv2 = ""
                    print("JOUEURS : ")
                    print (" Vous avez entré : " + clavier + " JOUEURS TOURNOIS EN COURS: r pour lecture, w pour création de joueurs, c pour charger")

                #création de la liste des joueurs
                if (menu_niv0 == "J" and clavier == "w"):
                    menu_niv1 = clavier
                    print ("création de la liste des joueurs, nom, prénom, date de naissance, sexe, classement")

                #affichage la liste des joueurs pour les sélectionner ensuite dans le tournoi
                if (menu_niv0 == "J" and clavier == "r"):
                    menu_niv1 = clavier

                #purge de la table des joueurs, utile pour debug
                if (menu_niv0 == "J" and clavier == "purge"):
                    menu_niv1 = clavier
                    print("vous allez purger la base de donnée des joueurs tapez :\"o\" pour confirmer")
                if (menu_niv0 == "J" and menu_niv1 == "purge" and clavier == "o"):
                    menu_niv2 = clavier

                #effacement un joueur de la liste si erreur de saisie
                if (menu_niv0 == "J" and clavier == "sup"):
                    menu_niv1 = clavier
                    print("vous voulez supprimer un joueur, suite à une erreur de saisie par exemple, de la liste des joueurs, tapez l'id du joueur à supprimer !")

                if (menu_niv0 == "J" and menu_niv1 == "sup" and clavier!="sup"):
                    menu_niv2 = clavier

                #****************************************************************
                # MENU ROUND
                if (clavier == "R"):
                    print(" touche 1 pour créer le 1er round, touche + pour créer les suivants")
                    menu_niv0 = clavier
                    menu_niv1 = ""
                    menu_niv2 = ""

                if (menu_niv0 == "R" and clavier == "1"):
                    menu_niv1 = clavier #; menu_niv2: ""
                    print (" Création d'un nouveau round :" + clavier + " Sélectionner le tournoi où les 8 joueurs ont été saisis")

                if (menu_niv0 == "R" and clavier == "+"):
                    menu_niv1 = clavier  # ; menu_niv2: ""
                    print(" Création d'un nouveau round :" + clavier + " Sélectionner le tournoi où les 8 joueurs ont été saisis")

                if (menu_niv0 == "R" and menu_niv0 == "+" and clavier != "+"):
                    menu_niv1 = clavier

                    # MENU MATCH
                if (clavier == "M"):
                    menu_niv0 = clavier; menu_niv1: ""; menu_niv2: ""
                    print (" Vous avez entré :"+ clavier + " MATCH : r pour lecture, w pour écriture; si écriture, "
                        "le round précédant se termine et la saisie des scores est à faire par paire")
                    #chronologiquement, la personne qui saisi doit repasser au 4 pour refaire des round, peut aussi se faire en automatiquement"
                    #si round 4, fin tournoi, mise à jour manuelle du classement des joueurs"
                    # création de la liste des joueurs
                if (menu_niv0 == "M" and clavier == "w"):
                    menu_niv1 = clavier
                    print("création du match")


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
            print("os._exit(0)")
            os._exit(0)


        print ("self.clavier")
        return (id_tournoi,clavier,menu_niv0,menu_niv1,menu_niv2)

    def Action_menu(self):
        from Controleur.Ctrl_Joueurs import creat_joueurs, lect_joueurs, sup_joueurs, purge_joueurs
        from Controleur.Ctrl_Tournoi import creat_tournois, lect_tournois, sup_tournois, purge_tournois,charge_joueurs_tournoi
        from Controleur.Ctrl_Round import creat_round_1
        from Vue.menu import ClassMainMenu

        saisie_clavier = ""
        menu_niv_0 = ""
        menu_niv_1 = ""
        menu_niv_2 = ""
        derniere_saisie = ""

        # essayer de voir s'il est possible d'appeler les fonctions directement dans le menu.py
        while (1 < 2):
            id_tournoi, saisie_clavier, menu_niv_0, menu_niv_1, menu_niv_2 = ClassMainMenu(id_tournoi="", clavier="",
                                                                                           niv0=menu_niv_0,
                                                                                           niv1=menu_niv_1,
                                                                                           niv2=menu_niv_2).CommandeClavier()
            print("return menu niv0 : " + menu_niv_0)
            print("return menu niv1 : " + menu_niv_1)
            print("return menu niv2 : " + menu_niv_2)
            # print("return id_tournoi : " + id_tournoi)

            if (menu_niv_0 == "J" and menu_niv_1 == "w" and saisie_clavier == "w"):
                # if (menu_niv_0 == "J"):
                print("Creation joueurs, retapez \"w\" une fois le 1er créé pour ressaisir le suivant")
                creat_joueurs()

            if (menu_niv_0 == "J" and menu_niv_1 == "r" and saisie_clavier == "r"):
                # if (menu_niv_0 == "J"):
                # print("joueurs dans la base de donnée :")
                lect_joueurs()

            if (menu_niv_0 == "J" and menu_niv_1 == "sup" and menu_niv_2 != ""):
                # if (menu_niv_0 == "J"):
                print("suppression d'un joueur")
                sup_joueurs(menu_niv_2)

            if (menu_niv_0 == "J" and menu_niv_1 == "purge"):
                # if (menu_niv_0 == "J"):
                print("Purge de la base de donnée des joueurs")
                purge_joueurs()

            if (menu_niv_0 == "T" and menu_niv_1 == "w" and saisie_clavier == "w"):
                # if (menu_niv_0 == "J"):
                print("Creation tournoi, tapez \"w\" ")
                creat_tournois()

            if (menu_niv_0 == "T" and menu_niv_1 == "r" and saisie_clavier == "r"):
                # if (menu_niv_0 == "J"):
                # print("joueurs dans la base de donnée :")
                lect_tournois()

            if (menu_niv_0 == "T" and menu_niv_1 == "sup" and menu_niv_2 != ""):
                # if (menu_niv_0 == "J"):
                print("suppression d'un tournoi")
                sup_tournois(menu_niv_2)

            if (menu_niv_0 == "T" and menu_niv_1 == "purge"):
                # if (menu_niv_0 == "J"):
                print("Purge de la base de donnée des joueurs")
                purge_tournois()

            if (menu_niv_0 == "T" and menu_niv_1 == "c" and saisie_clavier == "c"):
                charge_joueurs_tournoi()

            if (menu_niv_0 == "R" and menu_niv_1 == "1" and saisie_clavier == "1"):
                creat_round_1()

            if (menu_niv_0 == "R" and menu_niv_1 == "+" and saisie_clavier == "+"):
                creat_round_1()
