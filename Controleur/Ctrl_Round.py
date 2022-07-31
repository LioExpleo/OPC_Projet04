import os
import re
from Vue.menu import ClassMainMenu
from Modele.Tournoi import ClassTournoi
from Modele.Round import ClassRound
import time
import json

from tinydb import TinyDB, Query, where
Todo = Query()

db_round = TinyDB('round.json')


def creat_round_1():
        print ("Ctrl_Round - creat_round_1")
        print("inst_creat_round_1 = ClassRound.CreatRound_1(x)")
        x=""
        inst_creat_round_1 = ClassRound.CreatRound_1(x)


