from Controleur.main import main_control
from Vue.menu import ClassMainMenu
from Controleur.Ctrl_Joueurs import creat_joueurs,lect_joueurs,sup_joueurs,purge_joueurs
#from Controleur.Ctrl_Joueurs import lect_joueurs,sup_joueurs,purge_joueurs
from Controleur.Ctrl_Tournoi import creat_tournois,lect_tournois,sup_tournois,purge_tournois

saisie_clavier = ""
menu_niv_0 = ""
menu_niv_1 = ""
menu_niv_2 = ""
derniere_saisie = ""

#essayer de voir s'il est possible d'appeler les fonctions directement dans le menu.py
while (1<2):
    id_tournoi, saisie_clavier, menu_niv_0, menu_niv_1, menu_niv_2 = ClassMainMenu(id_tournoi="", clavier="",niv0=menu_niv_0, niv1=menu_niv_1,niv2=menu_niv_2).CommandeClavier()
    print("return menu niv0 : " + menu_niv_0)
    print("return menu niv1 : " + menu_niv_1)
    print("return menu niv2 : " + menu_niv_2)
    #print("return id_tournoi : " + id_tournoi)

    if (menu_niv_0 == "J" and menu_niv_1 == "w"):
    #if (menu_niv_0 == "J"):
        print("Creation joueurs, retapez \"w\" une fois le 1er créé pour ressaisir le suivant")
        creat_joueurs()

    if (menu_niv_0 == "J" and menu_niv_1 == "r"):
    #if (menu_niv_0 == "J"):
        print("joueurs dans la base de donnée :")
        lect_joueurs()

    if (menu_niv_0 == "J" and menu_niv_1 == "sup" and menu_niv_2 !=""):
    #if (menu_niv_0 == "J"):
        print("suppression d'un joueur")
        sup_joueurs(menu_niv_2)

    if (menu_niv_0 == "J" and menu_niv_1 == "purge"):
    #if (menu_niv_0 == "J"):
        print("Purge de la base de donnée des joueurs")
        purge_joueurs()

    if (menu_niv_0 == "T" and menu_niv_1 == "w"):
    #if (menu_niv_0 == "J"):
        print("Creation tournoi, tapez \"w\" ")
        creat_tournois()

    if (menu_niv_0 == "T" and menu_niv_1 == "r"):
    #if (menu_niv_0 == "J"):
        print("joueurs dans la base de donnée :")
        lect_tournois()

    if (menu_niv_0 == "T" and menu_niv_1 == "sup" and menu_niv_2 !=""):
    #if (menu_niv_0 == "J"):
        print("suppression d'un tournoi")
        sup_tournois(menu_niv_2)

    if (menu_niv_0 == "T" and menu_niv_1 == "purge"):
    #if (menu_niv_0 == "J"):
        print("Purge de la base de donnée des joueurs")
        purge_tournois()
