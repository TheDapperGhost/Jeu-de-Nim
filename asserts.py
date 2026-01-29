import joueur

def test_valider_coup():
    assert joueur.valider_coup(1) is True
    assert joueur.valider_coup(3) is True
    assert joueur.valider_coup(4) is False
    assert joueur.valider_coup(-1) is False

def test_tester_victoire():
    assert joueur.tester_victoire(3, 3) is True
    assert joueur.tester_victoire(2, 1) is False

test_valider_coup()
test_tester_victoire()
print("YAYYYY TOUT MARCHE")
