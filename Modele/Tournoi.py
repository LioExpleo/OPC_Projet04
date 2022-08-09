import json
from datetime import datetime
# noinspection PyUnresolvedReferences
from tinydb import TinyDB,Query,where

class ClassTournoi:
    def __init__(self):
        pass
    '''
    def CreatTournois(self):

        # identifiant tournoi
        import json
        from tinydb import TinyDB, Query, where
        Todo = Query()
        db_tournoi = TinyDB('tournois.json')
        mode_ouv_fichier_json = "r"
        with open('tournois.json', mode_ouv_fichier_json) as fichier_joueur:
            pass
        ''''''
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

        nom = input("saisie nom : \n")
        if nom == "":
            nom = ("Tournoi " + str(id_tournoi))
            print("en absence de nom, le nom par défaut est " + nom)
        if nom == "r":
            nom = ("Tournoi " + str(id_tournoi))
            print("r est un nom interdit, cela correspond à une commande clavier, le nom par défaut est " + nom)
        if nom == "E":
            nom = ("Tournoi " + str(id_tournoi))
            print(
                "E est un nom interdit, cela correspond à une commande clavier, le nom par défaut enregistré est " + nom)

        lieu = input("saisie lieu : \n")
        if lieu == "":
            lieu = ("Lieu " + str(id_tournoi))

        date = input("date (format DD/MM/YYYY): \n")
        if date =="":
            date_heure = datetime.now()
            str_date_heure = str(date_heure)
            char = '.'
            PositChar = str_date_heure.find(char)
            str_date_heure = str_date_heure[0:(PositChar-9)]
            date = str_date_heure

        nbr_rounds = input("saisie nombre de rounds, 4 rounds si pas de saisie ou erreur de saisie: \n")

        if nbr_rounds == "":
            nbr_rounds = "4"

        try:
            int_nbr_rounds = int(nbr_rounds)
        except ValueError:
            print("Nombre de round max = 7, mini = 1, 4 par défaut")
            int_nbr_rounds = 4
            nbr_rounds = "4"

        if int_nbr_rounds > 7 or int_nbr_rounds < 1:
            print("Nombre de round max = 7, mini = 1, 4 par défaut")
            nbr_rounds = "4"

        id_j1="";id_j2="";id_j3="";id_j4="";id_j5="";id_j6="";id_j7="";id_j8=""

        # Serialize l'instance tournoi
        tournoi = {"id_tournoi": id_tournoi,"nom": nom, "lieu": lieu, "date du tournoi": date,
                  "nombre de rounds": nbr_rounds, "id_j1":id_j1,"id_j2":id_j2,"id_j3":id_j3,"id_j4":id_j4,"id_j5":id_j5,"id_j6":id_j6,"id_j7":id_j7,"id_j8":id_j8,}

        db_tournois.insert(inst_creat_tournois)
        return (tournoi)
    '''
    def CreatNewTournois(self,tournoi):
        # insertion des données d'un tournoi dans la nase de donnée
        import json
        from tinydb import TinyDB, Query, where
        Todo = Query()
        db_tournois = TinyDB('tournois.json')
        mode_ouv_fichier_json = "a+"
        with open('tournois.json', mode_ouv_fichier_json) as fichier_joueur:
            db_tournois.insert(tournoi)

        return (tournoi)