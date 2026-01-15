#aae : allumettes à enlever
def jouer_coup(joueur : bool) -> int:
    """Demande au joueur de jouer son coup"""
    aae : int = int(input("Combien d'allumettes voulez-vous enlever (entre 1 et 3) ? : "))
    while valider_coup() is False:
        print("Entrez un nombre valide d'allumettes !")
        aae : int = int(input("Combien d'allumettes voulez-vous enlever (entre 1 et 3) ? : "))
    return aae
    


def valider_coup(aae: int) -> bool:
    """Vérifie si le coup joué est valide"""
    return  0 <= aae <=3
    


def tester_victoire(NbrAllumettes : int, aae: int) -> bool:
    """Teste si le coup résulte à une victoire"""
    return (NbrAllumettes-aae) <= 0