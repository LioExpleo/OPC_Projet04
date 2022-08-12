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
        print()
        print("paire 2")
        print(List_de_liste_joueur[2])
        print()
        print("paire 3")
        print(List_de_liste_joueur[3])
        print()
        print("paire 4")
        print(List_de_liste_joueur[4])


        #Saisie des scores de la paire 1
        str_liste_liste_joueur1 = str(List_de_liste_joueur[1][0])
        str_liste_liste_joueur2 = str(List_de_liste_joueur[1][1])
        self=""
        texteJ1 = "saisissez le score pour le 1er joueur du 1er Match"
        texteJ2 = "saisissez le score pour le 2eme joueur du 1er Match"
        saisie_score1,saisie_score2 =ClassVueAffichage.SaisieScore(self,str_liste_liste_joueur1,str_liste_liste_joueur2, texteJ1,texteJ2)
        print('saisie score 1 et 2 du match 1: ' + (saisie_score1) + " - " + saisie_score2)

        # Ajout dans la liste de l'id du joueur et de son score
        #joueur 1
        liste_paire1_j1 = []
        liste_paire1_j1.append(List_de_liste_joueur[1][0][0])
        liste_paire1_j1.append(saisie_score1)
        print (liste_paire1_j1)
        # joueur 2
        liste_paire1_j2 = []
        liste_paire1_j2.append(List_de_liste_joueur[1][1][0])
        liste_paire1_j2.append(saisie_score2)
        print(liste_paire1_j2)

        # Chaque match génèrera 1 tuple avec comme nom, « Tuple_ « Id_tournoi » & n°round & « idMatch(n°paire)» de 2 listes
        nom_tuple1 = "IdTournoi"+str(tournoi_select) + "_" + "Round"+str(round_en_cours)+ "_"  + "Match"+ "1"
        #print([((liste_paire1_j1[0],liste_paire1_j1[1],liste_paire1_j2[0],liste_paire1_j2[1]))])
        globals()[nom_tuple1]=((liste_paire1_j1[0], liste_paire1_j1[1], liste_paire1_j2[0], liste_paire1_j2[1]))
        print("globals()[nom_tuple1]")
        print(globals()[nom_tuple1])
        print("nom du tuple pour le développement :")
        str_nom_tuple1 = str(nom_tuple1)
        print(str_nom_tuple1)
        #print tuple avec le nom créé avec globals
        print("nom créé avec globals :" + str_nom_tuple1)
        print(globals()[nom_tuple1])
        print(str_nom_tuple1)
        print("my_tuple")
        my_tuple = ((liste_paire1_j1[0],liste_paire1_j1[1],liste_paire1_j2[0],liste_paire1_j2[1]))
        print (my_tuple)
        print("")

        # Saisie des scores de la paire 2
        str_liste_liste_joueur1 = str(List_de_liste_joueur[2][0])
        str_liste_liste_joueur2 = str(List_de_liste_joueur[2][1])
        self = ""
        texteJ1 = "saisissez le score pour le 1er joueur du 2ème Match"
        texteJ2 = "saisissez le score pour le 2eme joueur du 2ème Match"
        saisie_score3, saisie_score4 = ClassVueAffichage.SaisieScore(self, str_liste_liste_joueur1,
                                                str_liste_liste_joueur2, texteJ1, texteJ2)
        print('saisie score 1 et 2 du match 2: ' + (saisie_score3) + " - " + saisie_score4)

        # Ajout dans la liste de l'id du joueur et de son score
        # joueur 1
        liste_paire2_j1 = []
        liste_paire2_j1.append(List_de_liste_joueur[2][0][0])
        liste_paire2_j1.append(saisie_score3)
        print(liste_paire2_j1)
        # joueur 2
        liste_paire2_j2 = []
        liste_paire2_j2.append(List_de_liste_joueur[2][1][0])
        liste_paire2_j2.append(saisie_score4)
        print(liste_paire2_j2)

        # Chaque match génèrera 1 tuple avec comme nom, « Tuple_ « Id_tournoi » & n°round & « idMatch(n°paire)» de 2 listes
        nom_tuple2 = "IdTournoi"+str(tournoi_select) + "_" + "Round"+str(round_en_cours)+ "_"  + "Match"+ "2"
        print(nom_tuple2)
        globals()[nom_tuple2] = ((liste_paire2_j1[0], liste_paire2_j1[1], liste_paire2_j2[0], liste_paire2_j2[1]))
        print("globals()[nom_tuple2]")
        print(globals()[nom_tuple2])
        print("")

        # Saisie des scores de la paire 3
        str_liste_liste_joueur1 = str(List_de_liste_joueur[3][0])
        str_liste_liste_joueur2 = str(List_de_liste_joueur[3][1])
        self = ""
        texteJ1 = "saisissez le score pour le 1er joueur du 3ème Match"
        texteJ2 = "saisissez le score pour le 2eme joueur du 3ème Match"
        saisie_score5, saisie_score6 = ClassVueAffichage.SaisieScore(self, str_liste_liste_joueur1,
                                                                     str_liste_liste_joueur2, texteJ1, texteJ2)
        print('saisie score 1 et 2 du match 3: ' + (saisie_score5) + " - " + saisie_score6)

        # Ajout dans la liste de l'id du joueur et de son score
        # joueur 1
        liste_paire3_j1 = []
        liste_paire3_j1.append(List_de_liste_joueur[3][0][0])
        liste_paire3_j1.append(saisie_score5)
        print(liste_paire3_j1)
        # joueur 2
        liste_paire3_j2 = []
        liste_paire3_j2.append(List_de_liste_joueur[3][1][0])
        liste_paire3_j2.append(saisie_score6)
        print(liste_paire3_j2)

        # Chaque match génèrera 1 tuple avec comme nom, « Tuple_ « Id_tournoi » & n°round & « idMatch(n°paire)» de 2 listes
        nom_tuple3 = "IdTournoi"+str(tournoi_select) + "_" + "Round"+str(round_en_cours)+ "_"  + "Match"+ "3"
        print(nom_tuple3)
        globals()[nom_tuple3] = ((liste_paire3_j1[0], liste_paire3_j1[1], liste_paire3_j2[0], liste_paire3_j2[1]))
        print("globals()[nom_tuple3]")
        print(globals()[nom_tuple3])
        print("")

        # Saisie des scores de la paire 4
        str_liste_liste_joueur1 = str(List_de_liste_joueur[4][0])
        str_liste_liste_joueur2 = str(List_de_liste_joueur[4][1])
        self = ""
        texteJ1 = "saisissez le score pour le 1er joueur du 4ème Match"
        texteJ2 = "saisissez le score pour le 2eme joueur du 4ème Match"
        saisie_score7, saisie_score8 = ClassVueAffichage.SaisieScore(self, str_liste_liste_joueur1,
                                                                     str_liste_liste_joueur2, texteJ1, texteJ2)
        print('saisie score 1 et 2 du match 4: ' + (saisie_score7) + " - " + saisie_score8)

        # Ajout dans la liste de l'id du joueur et de son score
        # joueur 1
        liste_paire4_j1 = []
        liste_paire4_j1.append(List_de_liste_joueur[4][0][0])
        liste_paire4_j1.append(saisie_score7)
        print(liste_paire4_j1)
        # joueur 2
        liste_paire4_j2 = []
        liste_paire4_j2.append(List_de_liste_joueur[4][1][0])
        liste_paire4_j2.append(saisie_score8)
        print(liste_paire4_j2)

        # Chaque match génèrera 1 tuple avec comme nom, « Tuple_ « Id_tournoi » & n°round & « idMatch(n°paire)» de 2 listes
        nom_tuple4 = "IdTournoi"+str(tournoi_select) + "_" + "Round"+str(round_en_cours)+ "_"  + "Match"+ "4"
        print(nom_tuple4)
        globals()[nom_tuple4] = ((liste_paire4_j1[0], liste_paire4_j1[1], liste_paire4_j2[0], liste_paire4_j2[1]))
        print("globals()[nom_tuple4]")
        print(globals()[nom_tuple4])
        print("")

        from tinydb import TinyDB, Query, where
        db_tournois = TinyDB('tournois.json')
        print()
        print("numéro de tournoi")
        print(int_tournoi_select)
        print(round_select)

        #préparation  pour mise dans la base de donnée
        #joueur 1
        print(List_de_liste_joueur[1])
        liste_match1 = []
        #liste_match1.append(List_de_liste_joueur[1])
        liste_match1.append(globals()[nom_tuple1])
        print("liste_match1")
        print(liste_match1)

        # joueur 2
        print(List_de_liste_joueur[2])
        liste_match2 = []
        #liste_match2.append(List_de_liste_joueur[2])
        liste_match2.append(globals()[nom_tuple2])
        print("liste_match2")
        print(liste_match2)

        # joueur 3
        print(List_de_liste_joueur[3])
        liste_match3 = []
        #liste_match3.append(List_de_liste_joueur[3])
        liste_match3.append(globals()[nom_tuple3])
        print("liste_match3")
        print(liste_match3)

        # joueur 4
        print(List_de_liste_joueur[4])
        liste_match4 = []
        #liste_match4.append(List_de_liste_joueur[4])
        liste_match4.append(globals()[nom_tuple4])
        print("liste_match4")
        print(liste_match4)

        liste_4matchs=[]
        liste_4matchs.append("Paire 1")
        liste_4matchs.append(liste_match1)
        liste_4matchs.append("-")
        liste_4matchs.append("Paire 2")
        liste_4matchs.append(liste_match2)
        liste_4matchs.append("-")
        liste_4matchs.append("Paire 3")
        liste_4matchs.append(liste_match3)
        liste_4matchs.append("-")
        liste_4matchs.append("Paire 4")
        liste_4matchs.append(liste_match4)

        # mise de l'heure de fin du match pour la mettre dans la base de donnée du tournoi
        date_heure_fin = datetime.now()
        str_date_heure_fin = str(date_heure_fin)
        char = '.'
        PositChar = str_date_heure_fin.find(char)
        str_date_heure_fin = str_date_heure_fin[0:(PositChar)]
        print("fin round en cours "+ str(round_en_cours) + " : " +str_date_heure_fin)

        # chargment dans la base de données de la fin de match du round en cours
        nom_donne_fin_match=("fin round "+ str(round_en_cours))
        donne_fin_match = str_date_heure_fin
        db_tournois.update({nom_donne_fin_match: donne_fin_match}, Todo.id_tournoi == int_tournoi_select)

        # chargment dans la base de données des scores des 4 matchs du round
        nom_donnees= "ScoreMatchRound" + str(round_en_cours)
        print (nom_donnees)
        db_tournois.update({nom_donnees: liste_4matchs}, Todo.id_tournoi == int_tournoi_select)

        #IL FAUT MAINTENANT QUE LA FIN DE MATCH EST FAITE CREER LE ROUND SUIVANT A PARTIR DE CETTE FIN DE MATCH
        #A LA CREATION DU ROUND SUIVANT, VERIFIER QUE CE N'EST PAS LE DERNIER AVANT
        #UNE FOIS LE ROUND SUIVANT CREE, IL FAUDRA METTRE LE NUMERO DE ROUND EN COURS DANS LA BASE DE DONNEE



        # FAIRE UNE METHODE DANS MODELE ET L'APPELER ICI POUR RESPECT MVC
        # La sélection du round 1 est sauvegardée dans la base de données du tournoi, il faudra écraser l'instance avec le résultat en plus des matchs
        #*****************************************************
        #db_tournois.update({"round_1+match": liste_round_1}, Todo.id_tournoi == int_tournoi_select)
        # *****************************************************

        #Les tuples 1, 2, 3 et 4 contiennent toutes les données à mettre dans la base de données du tournoi.
        #Ajouter un champ avec le nom du tuple et son contenu dans la base de donnée
        #puis mettre l'heure de fin du round et lancer le 2eme round



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

