import os
import re
from Vue.menu import ClassMainMenu
from Modele.Tournoi import ClassTournoi
#from Modele.Round import ClassRound
import time
import json
from Controleur.fonctions import creat_dict,creat_list
from datetime import datetime
from Controleur.fonctions import tournoi_exist

from tinydb import TinyDB, Query, where
Todo = Query()

db_round = TinyDB('round.json')

def creat_round_1():
        from Controleur.Ctrl_Tournoi import select_tournoi
        print("CreatRound_1")
        liste_liste_class_joueur = []
        # select_tournoi=""
        tournoi_select = select_tournoi()
        print("Prochain round tournoi selectionné : " + tournoi_select)

        # Affichage du tournoi
        from tinydb import TinyDB, Query, where
        Todo = Query()
        db_tournois = TinyDB('tournois.json')
        db_joueurs = TinyDB('joueurs.json')
        print("db_tournois.search(where('id_tournoi')==tournoi_select")
        int_tournoi_select = int(tournoi_select)

        # charger le tournoi selectionné à partir de la base de données dans tournoi
        tournoi = (db_tournois.search(where('id_tournoi') == int_tournoi_select))
        print(tournoi)

        #Récupération des informations du fichier JSON du tournoi pour créer les rounds
        import json
        fileObject = open("tournois.json", "r")
        jsonContent = fileObject.read()
        aList = json.loads(jsonContent)

        id_t = (tournoi[0]['id_tournoi'])
        print("id tournoi : " + str(id_t))

        nom_t =(tournoi[0]['nom'])
        print("nom : " + nom_t)

        nb_r=(tournoi[0]['nombre de rounds'])
        print(nb_r + " rounds")

        list_id_joueur=[]

        id_j1=(tournoi[0]['id_j1'])
        print("id joueur 1 : " + id_j1)
        list_id_joueur.append(id_j1)

        id_j2 = (tournoi[0]['id_j2'])
        print("id joueur 2 : " + id_j2)
        list_id_joueur.append(id_j2)

        id_j3 = (tournoi[0]['id_j3'])
        print("id joueur 3 : " + id_j3)
        list_id_joueur.append(id_j3)

        id_j4 = (tournoi[0]['id_j4'])
        print("id joueur 4 : " + id_j4)
        list_id_joueur.append(id_j4)

        id_j5 = (tournoi[0]['id_j5'])
        print("id joueur 5 : " + id_j5)
        list_id_joueur.append(id_j5)

        id_j6 = (tournoi[0]['id_j6'])
        print("id joueur 6 : " + id_j6)
        list_id_joueur.append(id_j6)

        id_j7 = (tournoi[0]['id_j7'])
        print("id joueur 7 : " + id_j7)
        list_id_joueur.append(id_j7)

        id_j8 = (tournoi[0]['id_j8'])
        print("id joueur 8 : " + id_j8)
        list_id_joueur.append(id_j8)

        print("nombre de rounds")
        print(nb_r)

        db_joueurs = TinyDB('joueurs.json')
        index_joueur = 0
        while (index_joueur < 8):
                id_jx = "id_j" + str(index_joueur)

                print("id_joueur " + str(index_joueur) + ": ")
                id_joueur_en_cours = ""
                int_id_joueur_en_cours = ""
                try:
                        #id_joueur_en_cours = (dict_tournoi[id_jx])
                        id_joueur_en_cours = list_id_joueur[index_joueur]
                except ValueError:
                        print("Vous devez choisir un tournoi où les 8 joueurs sont chargés pour créer des rounds")
                        os._exit()

                try:
                        int_id_joueur_en_cours = int(id_joueur_en_cours)
                except ValueError:
                        print("Erreur, vous devez choisir un tournoi où les 8 joueurs sont chargés pour créer des rounds")
                        os._exit(0)

                joueur = (db_joueurs.search(where('id_joueur') == int_id_joueur_en_cours))
                dict_joueur = creat_dict(joueur)

                print("identifiant joueur :")
                round_id_joueur = (dict_joueur["id_joueur"])
                print(round_id_joueur)

                print("Nom :")
                print(dict_joueur["Nom"])
                round_nom_joueur = (dict_joueur["Nom"])

                print("Prénom :")
                print(dict_joueur["Prenom"])
                round_prenom_joueur = (dict_joueur["Prenom"])

                print("Né le :")
                print(dict_joueur["date de naissance"])

                print("Sexe :")
                print(dict_joueur["sexe"])

                print("Classement :")
                round_class_joueur = (dict_joueur["Classement"])
                print(round_class_joueur)

                liste_class_joueur = [round_id_joueur, int(round_class_joueur), round_nom_joueur, round_prenom_joueur]
                print("liste : id_joueur, classement joueur, nom, prenom")
                print(liste_class_joueur)
                liste_liste_class_joueur.append(liste_class_joueur)
                print(liste_liste_class_joueur)

                index_joueur = index_joueur + 1

#                print("FIN RECUPERATION DES DONNEES DU JOUEUR")

        print("liste_liste_class_joueur : ")
        print(liste_liste_class_joueur)

        #Mise des joueurs dans ordre décroissant
        from operator import itemgetter
        print("List A based on index 0: % s" % (sorted(liste_liste_class_joueur, key=itemgetter(1), reverse=True)))
        joueur_class_decroissant = (sorted(liste_liste_class_joueur, key=itemgetter(1), reverse=True))
        print(joueur_class_decroissant)

        # Mise en ordre des joueurs par classement, le classement étant la valeur en position "1" de la liste
        joueur_class_croissant = (sorted(liste_liste_class_joueur, key=itemgetter(1), reverse=False))
        print("Affichage joueur par classement croissant")
        print(joueur_class_croissant)

        print("Affichage des paires de joueurs par identifiant du round 1 \n")
        liste_paire_1 = []
        liste_paire_1.append(joueur_class_croissant[0])
        liste_paire_1.append(joueur_class_croissant[4])
        # print(liste_paire_1)
        print("Paire 1, par ordre de classement, 1er joueur contre 5ème")
        print("ID: " + str(liste_paire_1[0][0]) + " , Nom:" + str(liste_paire_1[0][2]) + " , Prénom : " + str(
                liste_paire_1[0][3]))
        print("VS")
        print("ID: " + str(liste_paire_1[1][0]) + " , Nom:" + str(liste_paire_1[1][2]) + " , Prénom : " + str(
                liste_paire_1[1][3]))
        print()

        liste_paire_2 = []
        liste_paire_2.append(joueur_class_croissant[1])
        liste_paire_2.append(joueur_class_croissant[5])
        # print(liste_paire_2)
        print("Paire 2, par ordre de classement, 2eme joueur contre 6ème")
        print("ID: " + str(liste_paire_2[0][0]) + " , Nom:" + str(liste_paire_2[0][2]) + " , Prénom : " + str(
                liste_paire_2[0][3]))
        print("VS")
        print("ID: " + str(liste_paire_2[1][0]) + " , Nom:" + str(liste_paire_2[1][2]) + " , Prénom : " + str(
                liste_paire_2[1][3]))
        print()

        liste_paire_3 = []
        liste_paire_3.append(joueur_class_croissant[2])
        liste_paire_3.append(joueur_class_croissant[6])
        # print(liste_paire_3)
        print("Paire 3, par ordre de classement, 3eme joueur contre 7ème")
        print("ID: " + str(liste_paire_3[0][0]) + " , Nom:" + str(liste_paire_3[0][2]) + " , Prénom : " + str(
                liste_paire_3[0][3]))
        print("VS")
        print("ID: " + str(liste_paire_3[1][0]) + " , Nom:" + str(liste_paire_3[1][2]) + " , Prénom : " + str(
                liste_paire_3[1][3]))
        print()

        liste_paire_4 = []
        liste_paire_4.append(joueur_class_croissant[3])
        liste_paire_4.append(joueur_class_croissant[7])
        # print(liste_paire_4)
        print("Paire 4, par ordre de classement, 4eme joueur contre 8ème")
        print("ID: " + str(liste_paire_4[0][0]) + " , Nom:" + str(liste_paire_4[0][2]) + " , Prénom : " + str(
                liste_paire_4[0][3]))
        print("ID")
        print("identifiant: " + str(liste_paire_4[1][0]) + " , Nom:" + str(liste_paire_4[1][2]) + " , Prénom : " + str(
                liste_paire_4[1][3]))
        print()
        print("********** FIN DE RECUPERATION DES JOUEURS POUR LES ROUNDS ********************")

        nom = input("saisie nom du Round, Round 1 si pas de saisie:\n")
        if (nom == ""):
                nom = "Round 1"

        #mise de l'heure de depart dans la liste pour la mettre dans la base de donnée du tournoi
        date_heure_debut = datetime.now()
        str_date_heure_debut = str(date_heure_debut)
        char = '.'
        PositChar = str_date_heure_debut.find(char)
        str_date_heure_debut = str_date_heure_debut[0:(PositChar)]
        print("début heure round : " + str_date_heure_debut)

        print(liste_paire_1)
        print(liste_paire_2)
        print(liste_paire_3)
        print(liste_paire_4)

        print("********* FIN CREATION ROUND 1 *************************")
        #print ("Ctrl_Round - creat_round_1")
        #print("inst_creat_round_1 = ClassRound.CreatRound_1(x)")

        #inst_creat_round_1 = ClassRound.CreatRound_1(self=True)
        #Stocker les instances de Round dans le tournoi
        liste_round_1=[]
        liste_round_1.append(str_date_heure_debut)
        liste_round_1.append(liste_paire_1)
        liste_round_1.append(liste_paire_2)
        liste_round_1.append(liste_paire_3)
        liste_round_1.append(liste_paire_4)
        print()
        print("liste_round_1")
        print(liste_round_1)

        from tinydb import TinyDB, Query, where
        db_tournois = TinyDB('tournois.json')
        print()
        print("numéro de tournoi")
        print(int_tournoi_select)

        #FAIRE UNE METHODE DANS MODELE ET L'APPELER ICI POUR RESPECT MVC
        #La sélection du round 1 est sauvegardée dans la base de données du tournoi, il faudra écraser l'instance avec le résultat en plus des matchs
        #Si round_1+match n'existe pas dans la nase de donnée, il est créé
        db_tournois.update({"round_1+match": liste_round_1}, Todo.id_tournoi == int_tournoi_select)
        #joueur_a_charger = joueur_a_charger + 1
        #Ecriture du round en cours dans la base de donnée du tournoi
        db_tournois.update({"round_en_cours": 1}, Todo.id_tournoi == int_tournoi_select)

        return()