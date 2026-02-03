from __future__ import annotations
import joueur
import plateau
import contextlib # bibliothèque de gestion de contextes d’exécution
depot = open("temp.txt", "w", encoding="utf-8") # ouverture du fichier
with contextlib.redirect_stdout(joueur): # redirection sortie standard
    help(joueur.jouer_coup)
    depot.close() # fermeture du fichier