import os
import plateau
import joueur
import vlc

url = './Canard.mp3'
sound = vlc.MediaPlayer(url)
sound.play() #erreur affichée mais n'est pas une erreur : Canard.mp3 n'est pas vide et le projet fonctionne.

def clear() -> None:
    os.system("cls" if os.name in ("nt", "dos") else "clear")
    pass
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


#plateau.generer_partie()
#joueur1 = True

#while not joueur.tester_victoire():
#    aae : int = int(input("Combien d'allumettes voulez-vous enlever (entre 1 et 3) ? : "))
#    joueur.jouer_coup(joueur, aae)
#    joueur1 = not joueur1