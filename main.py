import os
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

NbrAllumettes = plateau.generer_partie()
plateau.afficher_plateau(NbrAllumettes , 0)
aae = joueur.jouer_coup
if joueur.tester_victoire(aae) == True:
    NbrAllumettes = NbrAllumettes - aae
else:
    print("joueur ", str(not joueur), " a gagné")
    réponse = ""
    while réponse != "oui":
        réponse = input("Rejouer? ")


#plateau.generer_partie()
#joueur1 = True

#while not joueur.tester_victoire():
#    aae : int = int(input("Combien d'allumettes voulez-vous enlever (entre 1 et 3) ? : "))
#    joueur.jouer_coup(joueur, aae)
#    joueur1 = not joueur1