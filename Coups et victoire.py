def jouer_coup(joueur : str) -> None:
    aae = int(input("Combien d'allumettes voulez-vous retirer ?\n"))
    
def valider_coup(aae):
    if 3 >= aae > 0:
        return True
    return False
def victoire(plateau :list) -> bool:
    return len(plateau) == 1