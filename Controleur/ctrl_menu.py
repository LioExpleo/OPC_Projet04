import os

class ClassCtrlMenu():
    def Action_menu(self):
        from Controleur.Ctrl_Joueurs import lect_joueurs, sup_joueurs, purge_joueurs,creat_new_joueurs
        from Controleur.Ctrl_Tournoi import lect_tournois, sup_tournois, purge_tournois,charge_joueurs_tournoi,creat_new_tournois
        from Controleur.Ctrl_Round import creat_round_1
        from Vue.menu import ClassMainMenu

        #saisie_clavier = ""
        menu_niv_0 = ""
        menu_niv_1 = ""
        menu_niv_2 = ""
        #derniere_saisie = ""

        # essayer de voir s'il est possible d'appeler les fonctions directement dans le menu.py
        while (1 < 2):
            id_tournoi, saisie_clavier, menu_niv_0, menu_niv_1, menu_niv_2 = ClassMainMenu(id_tournoi="", clavier="",
                                                                                           niv0=menu_niv_0,
                                                                                           niv1=menu_niv_1,
                                                                                           niv2=menu_niv_2).CommandeClavier()

            if (menu_niv_0 == "J" and menu_niv_1 == "w" and saisie_clavier == "w"):
                creat_new_joueurs()

            if (menu_niv_0 == "J" and menu_niv_1 == "r" and saisie_clavier == "r"):
                lect_joueurs()

            if (menu_niv_0 == "J" and menu_niv_1 == "sup" and menu_niv_2 != ""):
                sup_joueurs(menu_niv_2)

            if (menu_niv_0 == "J" and menu_niv_1 == "purge"):
                purge_joueurs()

            if (menu_niv_0 == "T" and menu_niv_1 == "w" and saisie_clavier == "w"):
                creat_new_tournois()

            if (menu_niv_0 == "T" and menu_niv_1 == "r" and saisie_clavier == "r"):
                lect_tournois()

            if (menu_niv_0 == "T" and menu_niv_1 == "sup" and menu_niv_2 != ""):
                sup_tournois(menu_niv_2)

            if (menu_niv_0 == "T" and menu_niv_1 == "purge"):
                purge_tournois()

            if (menu_niv_0 == "T" and menu_niv_1 == "c" and saisie_clavier == "c"):
                charge_joueurs_tournoi()

            if (menu_niv_0 == "R" and menu_niv_1 == "+" and saisie_clavier == "+"):
                creat_round_1()
