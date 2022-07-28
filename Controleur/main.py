#from Controleur.Contrôleur_Joueurs import main_controleur_joueurs
from Vue.menu import ClassMainMenu
from Controleur.Test_Contrôleur_Joueurs import creat_joueurs
from Controleur.Test_Contrôleur_Joueurs import lect_joueurs

def main_control():

    saisie_clavier =""
    menu_niv_0 = ""
    menu_niv_1 = ""
    menu_niv_2 = ""
    derniere_saisie=""

    id_tournoi, saisie_clavier, menu_niv_0, menu_niv_1, menu_niv_2 = ClassMainMenu(id_tournoi="", clavier="",
    niv0=menu_niv_0, niv1=menu_niv_1, niv2=menu_niv_2).CommandeClavier()
    print("test return menu niv0 : " + menu_niv_0)
    print("return menu niv1 : " + menu_niv_1)
    print("return menu niv2 : " + menu_niv_2)
    print("return id_tournoi : " + id_tournoi)

    if (menu_niv_0 == "J" and menu_niv_1 == "w"):
        print("menu_niv_0 == J and menu_niv_1 == w")
        creat_joueurs()

    if (menu_niv_0 == "J" and menu_niv_1 == "r"):
        print("menu_niv_0 == J and menu_niv_1 == r")

        lect_joueurs()

#main_controleur_joueurs()
