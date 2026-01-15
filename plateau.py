


def generer_partie() -> int:
    """Génère une nouvelle partie"""
    NbrAllumettes = int(input("Commencer la partie avec combien d'allumettes: "))
    return NbrAllumettes

#from main import clear

def afficher_plateau(NbrAllumettes: int, aae: int) -> None:
    """Affiche le plateau mis à jour"""
    vide = ""
    allumette = "|"
    #clear()
    for n in range(aae):
        print(vide, end = "  ")
    for n in range(NbrAllumettes):
        print(allumette, end = " ")