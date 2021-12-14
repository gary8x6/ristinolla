vastaukset = ["1","2","3","4","5","6","7","8","9"]      #lista muodostaa pelialueen
vastaus = ""
valinta = 0
kulku = 0
peli = True                                             #peli pyörii kunnes, jompikumpi voittaa tai tasapeli

def pelialue(vastaukset):                               #tekee pelialueen vastaukset-listasta ja välimerkeistä
    print(vastaukset[0] + " | " + vastaukset[1] + " | " + vastaukset[2] + "\n--|---|--\n" + vastaukset[3] + " | " + vastaukset[4] + " | " + vastaukset[5] + "\n--|---|--\n" + vastaukset[6] + " | " + vastaukset[7] + " | " + vastaukset[8])

def onkonumero(valinta):                                #tarkistaa, onko syöte numero ja välillä 1-9
    while True:
        valinta = input("Valitse koordinaattinumero (1-9): ")
        if valinta.isdigit() and int(valinta) >= 1 and int(valinta) < 10:
            if vastaukset[int(valinta)-1] != "0" and vastaukset[int(valinta)-1] != "x": #tsekkaa onko paikka jo käytetty
                return(valinta)
            else:
                print("Paikka on jo käytetty!")
        else:
            print("Yritä uudestaan")

def onkoxtai0(vastaus):                                 #kysyy kumpi on vuorossa. Tässä pelissä pelaajat pitävät huolta omista vuoroistaan.
    while True:
        vastaus = input("Oletko X vai 0: ")
        if vastaus.lower() == "x" or vastaus == "0":
            return(vastaus)
        else:
            print("Yritä uudestaan")
        

def lisaavastaus(valinta, vastaus):                     #lisää vastauksen vastaukset-listaan
    vastaukset[int(valinta)-1] = vastaus

def tarkistus(peli):                                    #tarkistaa onko jossain mahdollisesti kolme samaa merkkiä peräkkäin, kahdeksan vaihtoehtoa ja tasapeli
    if vastaukset[0] == vastaukset[1] == vastaukset[2]:
        print(vastaukset[0] + " voitti pelin!")
        return(False)
    elif vastaukset[3] == vastaukset[4] == vastaukset[5]:
        print(vastaukset[3] + " voitti pelin!")
        return(False)
    elif vastaukset[6] == vastaukset[7] == vastaukset[8]:
        print(vastaukset[6] + " voitti pelin!")
        return(False)
    elif vastaukset[0] == vastaukset[3] == vastaukset[6]:
        print(vastaukset[0] + " voitti pelin!")
        return(False)
    elif vastaukset[1] == vastaukset[4] == vastaukset[7]:
        print(vastaukset[1]+ " voitti pelin!")
        return(False)
    elif vastaukset[2] == vastaukset[5] == vastaukset[8]:
        print(vastaukset[2] + " voitti pelin!")
        return(False)
    elif vastaukset[0] == vastaukset[4] == vastaukset[8]:
        print(vastaukset[0] + " voitti pelin!")
        return(False)
    elif vastaukset[2] == vastaukset[4] == vastaukset[6]:
        print(vastaukset[2] + " voitti pelin!")
        return(False)
    elif kulku == 9:
        print("Tasapeli")
        return(False)
    else:
        return(True)


print("Ristinollapeli")

pelialue(vastaukset)

while peli == True:                         #peli pyörii tämän loopin sisällä ja kutsuu funktioita vuorotellen
    kulku += 1                              #laskee kuinka monta vuoroa on mennyt, jos yhdeksän niin tasapeli
    valinta = onkonumero(valinta)
    vastaus = onkoxtai0(vastaus)
    lisaavastaus(valinta, vastaus)
    pelialue(vastaukset)
    peli = tarkistus(peli)
