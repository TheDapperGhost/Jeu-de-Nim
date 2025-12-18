import os

def clear():
    os.system("cls" if os.name in ("nt", "dos") else "clear")

def partie(nb_joueur : int, nb_allumettes : int, plateau : list) -> list:
    
    return plateau

def generer_plateau(nb_allumettes : int) -> list:
    plateau = []
    for i in range(nb_allumettes):
        plateau += "|"
        return plateau
