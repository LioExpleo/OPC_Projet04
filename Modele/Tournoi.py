import json
import datetime
# noinspection PyUnresolvedReferences
from tinydb import TinyDB,Query,where

class ClassTournoi:
    def __init__(self, id_tournoi,nom, lieu, date, nbr_rounds=4,id_j1=0,id_j2=0,id_j3=0,id_j4=0,id_j5=0,id_j6=0,id_j7=0,id_j8=0):
        self.id_tournoi = id_tournoi
        self.nom = nom
        self.lieu = lieu
        self.date = date
        self.nbr_rounds = nbr_rounds
        self.id_j1 = id_j1
        self.id_j2 = id_j2
        self.id_j3 = id_j3
        self.id_j4 = id_j4
        self.id_j5 = id_j5
        self.id_j6 = id_j6
        self.id_j7 = id_j7
        self.id_j8 = id_j8

    def CreatTournois(self):
        nom= input("saisie nom : \n")
        if nom=="":
            nom ="X"
            print("en absence de nom, le nom par défaut est \"X\"")
        if nom == "r":
            nom = "_x"
            print("r est un nom interdit, cela correspond à une commande clavier, le nom par défaut enregistré est \"_r\"")
        if nom == "E":
            nom = "_E"
            print("E est un nom interdit, cela correspond à une commande clavier, le nom par défaut enregistré est \"_E\"")

        lieu = input("saisie lieu : \n")
        date = input("date (format DD/MM/YYYY): \n")


        nbr_rounds = input("saisie nombre de rounds, 4 rounds si pas de saisie ou erreur de saisie: \n")

        if nbr_rounds =="":
            nbr_rounds ="4"

        try:
            int_nbr_rounds = int(nbr_rounds)
        except ValueError:
            print("Nombre de round max = 7, mini = 1, 4 par défaut")
            int_nbr_rounds = 4
            nbr_rounds="4"

        if int_nbr_rounds > 7 or int_nbr_rounds<1:
            print("Nombre de round max = 7, mini = 1, 4 par défaut")
            nbr_rounds = "4"

        # identifiant tournoi
        import json
        from tinydb import TinyDB, Query, where
        Todo = Query()
        db_tournoi = TinyDB('tournois.json')
        mode_ouv_fichier_json = "r"
        with open('tournois.json', mode_ouv_fichier_json) as fichier_joueur:
            print("")

        # Rechercher un id libre dans la base de donnée en incrémentant l'id de test jusqu'à trouver un ID libre
        tournoi_cherche = 1
        tournoi_trouve = 0
        id_libre = 0

        # Si l' id_tournoi_cherché n'est pas trouvé, on le prend pour le mettre à l'id du nouveau tournoi
        # sinon, on reboucle jusqu'a trouver un id libre. On commence par regarder si l'id 1 existe
        tournoi_trouve = db_tournoi.search(Todo.id_tournoi == tournoi_cherche)
        tournoi_trouv = str(tournoi_trouve)
        # recherche de la position de id_joueur dans la chaine
        char = 'id_tournoi'
        PositDebNbre = (tournoi_trouv.find(char))
        # recherche de la position de nom dans la chaine
        char = "nom"
        PositFinNbre = (tournoi_trouv.find(char))

        # Recherche de l'id à partir des positions précédentes et suivantes'
        id_tournoi = tournoi_trouv[(PositDebNbre + 12): (PositFinNbre - 3)]
        print("id_tournoi")
        print(id_tournoi)

        # tant que l'id cherché existe, on recherche jusqu'à en trouver un libre en l'incrémentant
        while (id_tournoi != ""):
            tournoi_cherche = tournoi_cherche + 1
            tournoi_trouve = db_tournoi.search(Todo.id_tournoi == tournoi_cherche)
            tournoi_trouv = str(tournoi_trouve)
            char = 'id_tournoi'
            PositDebNbre = (tournoi_trouv.find(char))

            print("PositDebNbre")
            print(PositDebNbre)
            char = "nom"
            PositFinNbre = (tournoi_trouv.find(char))
            print("PositFinNbre")
            print(PositFinNbre)

            id_tournoi = tournoi_trouv[(PositDebNbre + 12): (PositFinNbre - 3)]
            print("id_tournoi")
            print(id_tournoi)

        else:
            id_libre = tournoi_cherche

        id_tournoi = id_libre
        id_j1="";id_j2="";id_j3="";id_j4="";id_j5="";id_j6="";id_j7="";id_j8=""

        # Serialize l'instance tournoi
        tournoi = {"id_tournoi": id_tournoi,"nom": nom, "lieu": lieu, "date du tournoi": date,
                  "nombre de rounds": nbr_rounds, "id_j1":id_j1,"id_j2":id_j2,"id_j3":id_j3,"id_j4":id_j4,"id_j5":id_j5,"id_j6":id_j6,"id_j7":id_j7,"id_j8":id_j8,}

        return (tournoi)

