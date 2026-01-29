#aae = allumettes à enlever
def jouer_coup() -> int:
    """Demande au joueur de jouer son coup"""
    while True:
        aae_input = input("Combien d'allumettes voulez-vous enlever (entre 1 et 3) ? : ")
        if str(aae_input).isdigit():
            aae = int(aae_input)
        else:
            aae = 50
        if valider_coup(aae):
            return aae
        print("Entrez un nombre valide d'allumettes !")
    


def valider_coup(aae: int) -> bool:
    """Vérifie si le coup joué est valide"""
    return  0 <= aae <=3
    


def tester_victoire(NbrAllumettes : int, aae: int) -> bool:
    """Teste si le coup résulte à une victoire"""
    return (NbrAllumettes-aae) <= 0
