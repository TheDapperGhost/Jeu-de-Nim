import os
import plateau
import joueur
import mp3play

url = "./canard.mp3"
clip = mp3play.load(url)
clip.play()

def clear() -> None:
    os.system("cls" if os.name in ("nt", "dos") else "clear")

clear()

#while not joueur.tester_victoire(NbrAllumettes, aae):
#    aae : int = int(input("Combien d'allumettes voulez-vous enlever (entre 1 et 3) ? : "))
#    joueur.jouer_coup(joueur, aae)
#    joueur1 : bool = not joueur1
