import plateau
import joueur

def clear() -> None:
    os.system("cls" if os.name in ("nt", "dos") else "clear")

plateau.generer_partie()
joueur1 = True

while not joueur.tester_victoire():
    aae : int = int(input("Combien d'allumettes voulez-vous enlever (entre 1 et 3) ? : "))
    joueur.jouer_coup(joueur, aae)
    joueur1 = not joueur1
