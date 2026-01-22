import os
import plateau
import joueur


if os.name == 'nt' or os.name == 'dos':
    def clear() -> None:
        os.system("cls")
else:
    def clear() -> None:
        os.system('clear')

clear()

def nouvelle_partie() -> None:
    """Lance une nouvelle partie"""
    ae = 0
    NbrAllumettes = plateau.generer_partie()
    plateau.afficher_plateau(NbrAllumettes , 0)
    aae = joueur.jouer_coup()
    ae = ae + aae
    while joueur.tester_victoire(NbrAllumettes, aae) != True:
        NbrAllumettes = NbrAllumettes - aae
        plateau.afficher_plateau(NbrAllumettes , ae)
        aae = joueur.jouer_coup()
        ae = ae + aae
    
    if joueur:
        print("Le joueur 2 a gagné")
    else:
        print("Le joueur 1 a gagné")

nouvelle_partie()

réponse = input("Rejouer ? (Y/n)")
while réponse.lower() == "y" or réponse == "":
    nouvelle_partie()
    réponse = input("Rejouer ? (Y/n)")
else:
    exit()
