deutschland = [(0,1),(0,2),(0,3),
               (1,3),
               (2,3),(2,4),
               (3,5),(3,7),(3,8),(3,9),(3,10),
               (4,6),(4,9),(4,12),
               (7,8),(7,11),
               (8,10),(8,11),(8,13),(8,14),
               (9,10),(9,12),
               (10,12),(10,14),
               (11,15),(11,13),
               (12,14),
               (13,14)]

def gueltige_faerbung(faerbung,karte):
    for land0,land1 in karte:
        if land0<len(faerbung) and land1<len(faerbung) and faerbung[land0]==faerbung[land1]:
            return False
    return True 

def naechste_faerbungen(faerbung,farben):
    naechste = []
    for farbe in farben:
        naechste.append(faerbung+[farbe])
    return naechste 

def faerbe(karte,laenderanzahl,farben):
    return versuche_faerben(karte,laenderanzahl,farben,[])

def versuche_faerben(karte,laenderanzahl,farben,faerbung):
    if len(faerbung)==laenderanzahl:
        return faerbung 
    else:
        for naechste in naechste_faerbungen(faerbung,farben):
            if gueltige_faerbung(naechste,karte):
                ergebnis = versuche_faerben(karte,laenderanzahl,farben,naechste)
                if ergebnis:
                    return ergebnis
        return None

farben5 = ['rot','gelb','blau','gruen','orange']
print(faerbe(deutschland,16,farben5))

# Adjazenzmatrix
               #0 1 2 3 4
nordlaender = [[0,1,1,1,0], #0
               [1,0,0,1,0], #1
               [1,0,0,1,0], #2
               [1,1,1,0,1], #3
               [0,0,0,1,0]] #4

# Adjeszenzliste
nordlaender = {0: [1,2,3], 1: [0,3], 2: [0,3], 3: [0,1,2,4], 4: [3]} 
