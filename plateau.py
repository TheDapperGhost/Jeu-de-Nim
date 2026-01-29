from term_image.image import from_file

image = from_file("allumette.ico")

def generer_partie() -> int:
    """Génère une nouvelle partie"""
    print(image)
    NbrAllumettes = input("Commencer la partie avec combien d'allumettes: ")
    if str(NbrAllumettes).isdigit():
        NbrAllumettes = int(NbrAllumettes)
    else:
        while str(NbrAllumettes).isdigit() is False :
            print("Entrez un nombre valide d'allumettes !")
            NbrAllumettes = input("Commencer la partie avec combien d'allumettes: ")
    return int(NbrAllumettes)

#from main import clear

def afficher_plateau(NbrAllumettes: int, aae: int) -> None:
    """Affiche le plateau mis à jour"""
    vide = ""
    allumette = " 🕯️ "
    #clear()
    for n in range(aae):
        print(vide, end = "  ")
    for n in range(NbrAllumettes):
        print(allumette, end = " ")
