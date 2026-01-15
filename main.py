import plateau
import joueur

plateau.generer_partie()

while not joueur.tester_victoire():
    aae : int = int(input("Combien d'allumettes voulez-vous enlever (entre 1 et 3) ? : "))
    joueur.jouer_coup()