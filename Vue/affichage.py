import os

class ClassVueAffichage:
    def __init__(self):
        pass
        #self.texte=texte

    def Affichage(self,texte1,texte2,texte3):
            print(texte1)
            print(texte2)
            print(texte3)

    def Input(self,texte1):
            input_saisie = input(texte1 + "\n")

            return(input_saisie)