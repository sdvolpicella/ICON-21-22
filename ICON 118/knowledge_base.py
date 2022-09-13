from pyswip import Prolog

def createKB():

    kb = Prolog()

    kb.assertz("ospedale(ospedale_1)") # definizione degli ospedali
    kb.assertz("ospedale(ospedale_2)")
    kb.assertz("ospedale(ospedale_3)")
    kb.assertz("ospedale(ospedale_4)")
    kb.assertz("ospedale(ospedale_5)")

    kb.assertz("infermieri(ospedale_1, 6)") # definizione del numero di infermieri per ogni ospedale
    kb.assertz("infermieri(ospedale_2, 7)")
    kb.assertz("infermieri(ospedale_3, 5)")
    kb.assertz("infermieri(ospedale_4, 5)")
    kb.assertz("infermieri(ospedale_5, 7)")

    kb.assertz("medici(ospedale_1, 4)") # definizione del numero di medici per ogni ospedale
    kb.assertz("medici(ospedale_2, 5)")
    kb.assertz("medici(ospedale_3, 2)")
    kb.assertz("medici(ospedale_4, 2)")
    kb.assertz("medici(ospedale_5, 5)")

    kb.assertz("soccorritori(ospedale_1, 7)") # definizione del numero dei soccorritori per ogni ospedale
    kb.assertz("soccorritori(ospedale_2, 9)")
    kb.assertz("soccorritori(ospedale_3, 6)")
    kb.assertz("soccorritori(ospedale_4, 6)")
    kb.assertz("soccorritori(ospedale_5, 9)")

    kb.assertz("ambulanza_A(ospedale_1, 4)") # definizione del numero di ambulanze di tipo A per ogni ospedale
    kb.assertz("ambulanza_A(ospedale_2, 7)")
    kb.assertz("ambulanza_A(ospedale_3, 5)")
    kb.assertz("ambulanza_A(ospedale_4, 5)")
    kb.assertz("ambulanza_A(ospedale_5, 7)")

    kb.assertz("ambulanza_B(ospedale_1, 3)") # definizione del numero di ambulanze di tipo B per ogni ospedale
    kb.assertz("ambulanza_B(ospedale_2, 5)")
    kb.assertz("ambulanza_B(ospedale_3, 4)")
    kb.assertz("ambulanza_B(ospedale_4, 4)")
    kb.assertz("ambulanza_B(ospedale_5, 5)")

    kb.assertz("ambulanza_C(ospedale_1, 1)") # definizione del numero di ambulanze di tipo C per ogni ospedale
    kb.assertz("ambulanza_C(ospedale_2, 3)")
    kb.assertz("ambulanza_C(ospedale_3, 2)")
    kb.assertz("ambulanza_C(ospedale_4, 2)")
    kb.assertz("ambulanza_C(ospedale_5, 3)")

    kb.assertz("ambulanza_SSP(ospedale_1, 3)") # definizione del numero di ambulanze di tipo SSP per ogni ospedale
    kb.assertz("ambulanza_SSP(ospedale_2, 7)")
    kb.assertz("ambulanza_SSP(ospedale_3, 5)")
    kb.assertz("ambulanza_SSP(ospedale_4, 5)")
    kb.assertz("ambulanza_SSP(ospedale_5, 7)")

    # Per ogni ospedale si definiscono i reparti presenti

    kb.assertz("gestione(ospedale_1, rianimazione, 1)")
    kb.assertz("gestione(ospedale_1, psichiatria, 0)")
    kb.assertz("gestione(ospedale_1, ortopedia, 1)")
    kb.assertz("gestione(ospedale_1, cardiologia, 1)")
    kb.assertz("gestione(ospedale_1, pneumologia, 1)")
    kb.assertz("gestione(ospedale_1, neurologia, 1)")
    kb.assertz("gestione(ospedale_1, oncologia, 0)")
    kb.assertz("gestione(ospedale_1, medicina, 1)")
    kb.assertz("gestione(ospedale_1, gastroenterologia, 0)")

    kb.assertz("gestione(ospedale_2, rianimazione, 1)")
    kb.assertz("gestione(ospedale_2, psichiatria, 1)")
    kb.assertz("gestione(ospedale_2, ortopedia, 0)")
    kb.assertz("gestione(ospedale_2, cardiologia, 1)")
    kb.assertz("gestione(ospedale_2, pneumologia, 1)")
    kb.assertz("gestione(ospedale_2, neurologia, 1)")
    kb.assertz("gestione(ospedale_2, oncologia, 1)")
    kb.assertz("gestione(ospedale_2, medicina, 1)")
    kb.assertz("gestione(ospedale_2, gastroenterologia, 0)")


    kb.assertz("gestione(ospedale_3, rianimazione, 1)")
    kb.assertz("gestione(ospedale_3, psichiatria, 0)")
    kb.assertz("gestione(ospedale_3, ortopedia, 0)")
    kb.assertz("gestione(ospedale_3, cardiologia, 1)")
    kb.assertz("gestione(ospedale_3, pneumologia, 0)")
    kb.assertz("gestione(ospedale_3, neurologia, 0)")
    kb.assertz("gestione(ospedale_3, oncologia, 0)")
    kb.assertz("gestione(ospedale_3, medicina, 1)")
    kb.assertz("gestione(ospedale_3, gastroenterologia, 0)")


    kb.assertz("gestione(ospedale_4, rianimazione, 0)")
    kb.assertz("gestione(ospedale_4, psichiatria, 1)")
    kb.assertz("gestione(ospedale_4, ortopedia, 0)")
    kb.assertz("gestione(ospedale_4, cardiologia, 0)")
    kb.assertz("gestione(ospedale_4, pneumologia, 0)")
    kb.assertz("gestione(ospedale_4, neurologia, 1)")
    kb.assertz("gestione(ospedale_4, oncologia, 0)")
    kb.assertz("gestione(ospedale_4, medicina, 1)")
    kb.assertz("gestione(ospedale_4, gastroenterologia, 0)")


    kb.assertz("gestione(ospedale_5, rianimazione, 1)")
    kb.assertz("gestione(ospedale_5, psichiatria, 0)")
    kb.assertz("gestione(ospedale_5, ortopedia, 1)")
    kb.assertz("gestione(ospedale_5, cardiologia, 1)")
    kb.assertz("gestione(ospedale_5, pneumologia, 1)")
    kb.assertz("gestione(ospedale_5, neurologia, 1)")
    kb.assertz("gestione(ospedale_5, oncologia, 0)")
    kb.assertz("gestione(ospedale_5, medicina, 1)")
    kb.assertz("gestione(ospedale_5, gastroenterologia, 1)")


    return kb