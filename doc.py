from __future__ import annotations
import joueur
import plateau
import io
import contextlib

# Capture de la documentation
output = io.StringIO()

with contextlib.redirect_stdout(output):
    print("=== Documentation de joueur.jouer_coup ===")
    help(joueur.jouer_coup)
    print("\n=== Documentation de joueur.valider_coup ===")
    help(joueur.valider_coup)
    print("\n=== Documentation de joueur.tester_victoire ===")
    help(joueur.tester_victoire)
    print("\n=== Documentation de plateau.generer_partie ===")
    help(plateau.generer_partie)
    print("\n=== Documentation de plateau.afficher_plateau ===")
    help(plateau.afficher_plateau)

# Écriture dans le fichier
with open("temp.txt", "w", encoding="utf-8") as depot:
    depot.write(output.getvalue())

depot = open("temp.txt", "w", encoding="utf-8")
with contextlib.redirect_stdout(depot):
    help(joueur)
    help(plateau)
depot.close()