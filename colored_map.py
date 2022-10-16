deutschland = [(0,1),(0,2),(0,3),              # 0: Schleswig-Holstein
               (1,3),                          # 1: Hamburg
               (2,3),(2,4),                    # 2: Mecklenburg-Vorpommern
               (3,5),(3,7),(3,8),(3,9),(3,10), # 3: Niedersachesn
               (4,6),(4,9),(4,12),             # 4: Brandenburg
                                               # 5: Bremen
                                               # 6: Berlin
               (7,8),(7,11),                   # 7: NRW
               (8,10),(8,11),(8,13),(8,14),    # 8: Hessen
               (9,10),(9,12),                  # 9: Sachsen-Anhalt
               (10,12),(10,14),                # 10: Thüringen
               (11,15),(11,13),                # 11: Rheinland-Pfalz
               (12,14),                        # 12: Sachsen
               (13,14)                         # 13: Baden-Würtemberg
                                               # 14: Bayern
                                               # 15: Saarland
              ]

farben2 = ['rot','gelb']
farben3 = ['rot','gelb','blau']
farben4 = ['rot','gelb','blau','gruen']
farben5 = ['rot','gelb','blau','gruen','orange']

def gueltige_faerbung(faerbung,karte):
        for land_1,land_2 in karte:
            if land_2<len(faerbung) and land_1<len(faerbung) and faerbung[land_1]==faerbung[land_2]:
                return False
        return True

def naechste_faerbung(faerbung,farben):
    naechste = []
    for farbe in farben:
        naechste.append(faerbung+[farbe])
    return naechste

def faerbe(karte,laenderanzahl,farben):
    loesungen = []
    anzahl = loesen(karte,laenderanzahl,farben,[],loesungen)
    return loesungen,anzahl

def loesen(karte,laenderanzahl,farben,faerbung,loesungen):
    if len(faerbung)==laenderanzahl:
        loesungen += [faerbung]
        return 1
    else:
        anzahl = 0
        for vorschlag in naechste_faerbung(faerbung,farben):
            if gueltige_faerbung(vorschlag,karte):
                anzahl += loesen(karte,laenderanzahl,farben,vorschlag,loesungen)

        return anzahl

print(faerbe(deutschland,16,farben4))
