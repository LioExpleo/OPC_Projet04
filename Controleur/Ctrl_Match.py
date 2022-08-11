"""création des joueurs - appel du modele joueur lors de la création des joueurs"""
"""affichage liste joueurs de la base de donnée, suppression d'un joueur de la base de donnée, purge de la base de donnée"""
import os
import re
from Vue.menu import ClassMainMenu
from Modele.Tournoi import ClassTournoi
import time
import json
from Vue.affichage import ClassVueAffichage
from tinydb import TinyDB, Query, where
from datetime import datetime
Todo = Query()

#db_tournois = TinyDB('tournois.json')

def creat_match():
        from Controleur.Ctrl_Tournoi import select_tournoi
        print("saisie des scores du match")
        # faire un input pour indiquer le tournoi à sélectionner
        #saisie_tournoi = (input("Tournoi ? : \n"))

        #Vérifier que la saisie du numero du tournoi est correcte
        tournoi_select = select_tournoi()

        # charger le tournoi selectionné à partir de la base de données dans tournoi
        #tournoi = (db_tournois.search(where('id_tournoi') == tournoi_select))
        #print(tournoi)

        #tournoi_select = select_tournoi()
        from tinydb import TinyDB, Query, where
        Todo = Query()
        db_tournois = TinyDB('tournois.json')
        int_tournoi_select = int(tournoi_select)

        print("int_tournoi_select")
        print (int_tournoi_select)

        tournoi = (db_tournois.search(where('id_tournoi') == int_tournoi_select))
        print(tournoi)

        # Récupération des informations du fichier JSON du tournoi pour vérifier le round en cours
        import json
        fileObject = open("tournois.json", "r")
        jsonContent = fileObject.read()
        aList = json.loads(jsonContent)


        id_t = (tournoi[0]['id_tournoi'])
        print("id tournoi : " + str(id_t))

        round_en_cours = (tournoi[0]['round_en_cours'])
        print("round_en_cours : " + str(round_en_cours))

        List_de_liste_joueur = (tournoi[0]['round_en_cours'])
        round_select= "round_"+str(round_en_cours)+"+match"
        print(round_select)

        #aller chercher les listes en fonction du round en cours
        List_de_liste_joueur = (tournoi[0][round_select])
        print ("List_de_liste_joueur")
        print(List_de_liste_joueur)
        print()
        print("paire 1")
        print(List_de_liste_joueur[1])
        print("paire 2")
        print(List_de_liste_joueur[2])
        print("paire 1")
        print(List_de_liste_joueur[3])
        print("paire 1")
        print(List_de_liste_joueur[4])


        #Saisie des scores de la paire 1
        str_liste_liste_joueur1 = str(List_de_liste_joueur[1][0])
        str_liste_liste_joueur2 = str(List_de_liste_joueur[1][1])
        self=""
        texteJ1 = "saisissez le score pour le 1er joueur du 1er Match"
        texteJ2 = "saisissez le score pour le 2eme joueur du 1er Match"
        saisie_score1,saisie_score2 =ClassVueAffichage.SaisieScore(self,str_liste_liste_joueur1,str_liste_liste_joueur2, texteJ1,texteJ2)
        print('saisie score 1 et 2 du match 1: ' + (saisie_score1) + " - " + saisie_score2)

        # Saisie des scores de la paire 2
        str_liste_liste_joueur1 = str(List_de_liste_joueur[2][0])
        str_liste_liste_joueur2 = str(List_de_liste_joueur[2][1])
        self = ""
        texteJ1 = "saisissez le score pour le 1er joueur du 2ème Match"
        texteJ2 = "saisissez le score pour le 2eme joueur du 2ème Match"
        saisie_score3, saisie_score4 = ClassVueAffichage.SaisieScore(self, str_liste_liste_joueur1,
                                                str_liste_liste_joueur2, texteJ1, texteJ2)
        print('saisie score 1 et 2 du match 2: ' + (saisie_score1) + " - " + saisie_score2)

        # Saisie des scores de la paire 3
        str_liste_liste_joueur1 = str(List_de_liste_joueur[3][0])
        str_liste_liste_joueur2 = str(List_de_liste_joueur[3][1])
        self = ""
        texteJ1 = "saisissez le score pour le 1er joueur du 3ème Match"
        texteJ2 = "saisissez le score pour le 2eme joueur du 3ème Match"
        saisie_score5, saisie_score6 = ClassVueAffichage.SaisieScore(self, str_liste_liste_joueur1,
                                                                     str_liste_liste_joueur2, texteJ1, texteJ2)
        print('saisie score 1 et 2 du match 3: ' + (saisie_score5) + " - " + saisie_score6)

        # Saisie des scores de la paire 4
        str_liste_liste_joueur1 = str(List_de_liste_joueur[4][0])
        str_liste_liste_joueur2 = str(List_de_liste_joueur[4][1])
        self = ""
        texteJ1 = "saisissez le score pour le 1er joueur du 4ème Match"
        texteJ2 = "saisissez le score pour le 2eme joueur du 4ème Match"
        saisie_score1, saisie_score2 = ClassVueAffichage.SaisieScore(self, str_liste_liste_joueur1,
                                                                     str_liste_liste_joueur2, texteJ1, texteJ2)
        print('saisie score 1 et 2 du match 4: ' + (saisie_score1) + " - " + saisie_score2)



        #Chaque match génèrera 1 tuple avec comme nom, « Tuple_ « Id_tournoi » & n°round & « idMatch(n°paire)» de 2 listes
        #Chaque tuple contiendra 2 listes :
        #La liste 1, id_joueur1 et score joueur 1.
        #La liste 2, id_joueur2 et score joueur 2.
        # Stocker les instances de round dans le tournoi.

        #une fois les 4 scores saisis, (tuple de listes) l'heure de fin du round est mis dans la base de donnée,
        # attention à la position des nouvelles valeurs dans la base de donnée, écrire les nouvelles infos à la fin
        #chargement des tuples dans la base de donnée
        #la génération du round suivant est générée, et le round en cours indiqué + 1 jusqu'à la fin des rounds.


#générer nom tuple : Tuple + id_tournoi+numéro round+ numéro de paire
#liste 1 : id_joueur_1 + score joueur 1
#liste 2 : id_joueur_2 + score joueur 2

#ECRIRE HEURE ARRET DU ROUND QUAND SCORES SAISIS DES 4 MATCHS DANS LA LISTE ROUND DANS LE TOURNOI

