import os
#Appel du prog qui gère les différents menus du programme
#Import à partir de directory -Vue- et du prog -menu- de la classe -MainMenu-

#from Controleur.main import



#sera a mettre dans contrôleur
from Modele.Joueurs import ClassJoueurs

info_saisies =""

#MainMenu()
poubelle =""
inst_creat_joueurs = ClassJoueurs.CreatJoueurs(poubelle)

print()
print ("inst_creat_joueurs")
print(inst_creat_joueurs)

#serialized_inst_creat_joueurs = inst_creat_joueurs
#print(serialized_inst_creat_joueurs)


# TinyDB - Représente ta base de donnée
# Query - Permet d'interroger ta base de donnée
# where - Permet d'affiner tes critères de recherche
from tinydb import TinyDB,Query,where
Todo=Query()

#Création de la table db_joueurs
db_joueurs = TinyDB('db.json')

#purge de la table
db_joueurs.truncate()

#Insertion du joueur saisi dans la base de donnée
db_joueurs.insert(inst_creat_joueurs)

#Exemple Comment écrire dans la table à partir d'une variable :
Prenom= "Renéeeeeeeeeeeeeeeeeeeeeeeeeeee"
#insertion des joueurs dans la table db_joueurs
db_joueurs.insert({'nom': 'DUPONT', 'prénom':Prenom,'date_naissance': '01/01/2000', 'sexe': 'f','classement':'100', 'score_total':'2', 'score_round':'0.5'})
db_joueurs.insert(inst_creat_joueurs)
db_joueurs.insert(inst_creat_joueurs)
db_joueurs.insert(inst_creat_joueurs)
db_joueurs.insert(inst_creat_joueurs)

print()


#Exemple de comment extraire une donnée précise de la table pour l'exploiter
import json
with open('db.json') as mon_fichier:
    dico=json.load(mon_fichier)

print("data dico")
print(dico)
nom_dico=(dico["_default"]["1"]["nom"])
print("dico nom : "+ nom_dico)

prénom_dico=(dico["_default"]["1"]["prénom"])
print("dico prénom : "+ prénom_dico)

date_naissance_dico=(dico["_default"]["1"]["date de naissance"])
print("dico date_naissance : "+ date_naissance_dico)

sexe_dico=(dico["_default"]["1"]["sexe"])
print("dico sexe : "+ sexe_dico)

classement_dico=(dico["_default"]["1"]["classement"])
print("dico classement : "+ classement_dico)

#score_total_dico=(dico["_default"]["1"]["score_total"])
#print("dico score_total : "+ score_total_dico)

#score_round_dico=(dico["_default"]["1"]["score_round"])
#print("dico score_round : "+ score_round_dico)

print()

print(db_joueurs.search(Todo.nom == 'Duchnoc'))



#xtest contient uniqueement les données de duchnoc
xtest = (db_joueurs.search(Todo.nom == 'Duchnoc'))
print(xtest)


mon_dict = {"nom": "Person", "prenom": "Paul"}
nom = mon_dict["nom"]
prenom = mon_dict["prenom"]
print (nom)
print (prenom)

print()

#N'affiche que les DUPONT
print (db_joueurs.search(where('nom') == 'DUPONT'))
print()

#affichage de tous les éléments de la table
print(db_joueurs.all())
print()

from Vue.menu import ClassMainMenu
#Import à partir de directory -Modele- et du prog -Tournoi- de la classe -Tournoi-

#Import à partir de directory -Modele- et du prog -Joueurs- de la classe -Joueurs-

#Import à partir de directory -Modele- et du prog -Rondes- de la classe -Rondes-

#Import à partir de directory -Modele- et du prog -Match- de la classe -Match-
#from Modele.Joueurs import Joueurs



id_tournoi = ""
saisie_clavier =""
menu_niv_0 = ""
menu_niv_1 = ""
menu_niv_2 = ""
derniere_saisie=""
Joueurs=""

while (saisie_clavier!="E"):
    #Lancer la méthode CommandeClavier de la classe MainMenu
    id_tournoi,saisie_clavier, menu_niv_0, menu_niv_1, menu_niv_2 = ClassMainMenu(id_tournoi="", clavier="",niv0=menu_niv_0,niv1=menu_niv_1,niv2=menu_niv_2 ).CommandeClavier()
    print ("menu niv0 : "+ menu_niv_0)
    print("menu niv1 : " + menu_niv_1)
    print("menu niv2 : " + menu_niv_2)
    print("id_tournoi : " + id_tournoi)

    #print ("récupération de la valeur entrée au clavier : " + saisie_clavier )

    # Création ou affichage ou chargement tournoi
    # Création
    if (menu_niv_0 == "1" and menu_niv_1=="w"):
        print("Création de l'appel de la méthode de la classe pour créer un nouveau tournoi")
        # tournoi = créer_tournoi()

    # Affichage de la liste
    if (menu_niv_0 == "1" and menu_niv_1 =="r"):
        print("Création de l'appel de la méthode de la classe pour afficher la liste des tournois")
        #print ("appel de la méthode de la classe pour créer ou afficher la liste des tournois")
        #print("r pour afficher la liste des tournois - w pour créer un nouveau tournoi")

    # Affichage de la liste
    if (menu_niv_0 == "1" and menu_niv_1 == "c"):
        print("Création de l'appel de la méthode de la classe pour charger un tournoi")

    # Création ou affichage des joueurs du tournoi
    if (menu_niv_0 == "2" and menu_niv_1 =="w"):

        #nom,prénom=Joueurs(nom="azert",prénom="").CreatJoueurs()
        #Joueurs(nom="azert",prénom="", date_naissance="01/01/2001",sexe="x",classement="0",score_total="0",score_round="0").CreatJoueurs()

        print ("appel de la méthode de la classe pour créer les joueurs")
        #joueurs = créer_joueurs()
    if (derniere_saisie == "2" and saisie_clavier == "+"):
        print("Passage au champs de saisie suivant")

    if saisie_clavier == "3":
        menu_niv_0 = saisie_clavier


    avant_deniere_saisie = derniere_saisie
    derniere_saisie = saisie_clavier

else:
    os._exit(0)