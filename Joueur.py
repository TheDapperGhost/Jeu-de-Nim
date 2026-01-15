from main import clear

#aae : allumettes à enlever
def jouer_coup(joueur, aae : int) -> int:
    """Demande au joueur de jouer son coup"""
    while valider_coup() is False:
        print("Entrez un nombre valide d'allumettes !")
        aae : int = int(input("Combien d'allumettes voulez-vous enlever (entre 1 et 3) ? : "))
    clear()
    print(f"{"|"*(NbrAllumettes-aae)}")
    return aae
    


def valider_coup(aae: int) -> bool:
    """Vérifie si le coup joué est valide"""
    if 1 <= aae <= 3:
        return True
    return False
    


def tester_victoire(aae: int) -> bool:
    """Teste si le coup résulte à une victoire"""
    
