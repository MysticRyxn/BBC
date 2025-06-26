# programma KentekenCheck
# Versie: 1.2
# Auteur: B. van der Feen
# Edit: M. van Hoek
# Datum:  14/7/2022
#
#

from datetime import datetime
import os

# OPDRACHT
#
# Maak de variabele appPath aan en gebruik die om op één plek om het pad te definieren voor alle bestanden.
# Gebruik vervolgens appPath overal bij het verwijzen naar het pad van de bestanden.
# Doe dit voor eventuele nieuwe verwijzingen én vervang de bestaande verwijzingen in deze code.
appPath = r"C:\Users\administrator\KentekenCheck\\"
rdwFile = os.path.join(appPath, "RDW.csv")
scanFile = os.path.join(appPath, "GescandeData.csv")
valsFile = os.path.join(appPath, "vals.txt")

print("= = =  programma kentekensignalering gestart = = = ") 

# OPDRACHT
# Druk de huidige datum en tijd af
current_datetime = datetime.now()
print("Huidige datum:", current_datetime.date())
print("Huidige tijd:", current_datetime.time())

rdwInput = open("C:\\Users\\administrator\\KentekenCheck\\RDW.csv")
scanInput = open("C:\\Users\\administrator\\KentekenCheck\\GescandeData.csv")
aantalVerwerkt = aantalFout = 0
legenVals = ""

# OPDRACHT
#
# Vraag hier of het bestand vals.txt leeg gemaakt moet worden (j of n)
legenVals = input("Wil je het bestand vals.txt leegmaken? (j of n): ").lower()
# Sla de keuze op in de variabele legenVals


if legenVals  == "n":       #open nieuw, of toevoegen aan vals.txt
    signaleringen = open("C:\\Users\\administrator\\KentekenCheck\\" , "a")
else:
    signaleringen = open("C:\\Users\\administrator\\KentekenCheck\\" , "w")


for auto in scanInput:       #lezen rij voor rij vanuit ScanDevice - GescandeData.csv
    if len(auto) < 10:       #Records korter dan 10 overslaan
        continue
                                 
    autoDelen = auto.split(",") #Record opsplitsen in losse velden van tabel autoDelen 
    scanKenteken = autoDelen[0]
    scanMerk = autoDelen[1]
    scanType = autoDelen[2]
    scanType = scanType.replace("\n", "")  #vervang de eventuele \n achter type
    aantalVerwerkt = aantalVerwerkt + 1
    
    match = 0                   #er is nog geen match gevonden
    rdwInput.seek(0)            #starten aan het begin van het bestand
    for rdwAuto in rdwInput:    #lezen rij voor rij uit RDW.csv
        rdwAutoDelen=rdwAuto.split(",")
        rdwKenteken = rdwAutoDelen[0]
        rdwMerk = rdwAutoDelen[2]
        rdwType = rdwAutoDelen[3]

        # OPDRACHT
        #
        # Als kentekens overeenkomen, dan wordt match op 1 gezet
        if scanKenteken == rdwKenteken:  #kenteken komt overeen
            match = 1
        # en moet gestopt worden met zoeken in RDW.txt
            break
                       
    if match == 0:              #einde bestand bereikt en kenteken onbekend
        aantalFout = aantalFout + 1
        print ("Onbekend kenteken: ", scanKenteken, scanMerk, scanType, "\n\n")
        signaleringen.write("Onbekend," + scanKenteken + "," + scanMerk + "," + scanType + "\n")
    else:                       #kenteken gevonden
        if scanMerk != rdwMerk or scanType != rdwType:  #merk of type onjuist
            aantalFout=aantalFout + 1
            print ("Onjuist kenteken:", scanKenteken, scanMerk, scanType)
            print ("Geregistreerd op:", rdwKenteken, rdwMerk, rdwType, "\n\n")
            signaleringen.write("Onjuist," + scanKenteken + "," + scanMerk + "," + scanType + "\n")
                                #afsluitend de aantallen weergeven
print("Eindtotalen KentekenCheck" )

# OPDRACHT
#
# print het aantal correcte kentekens
# print het aantal onjuiste kentekens
print("Eindtotalen KentekenCheck")
print("Aantal correcte kentekens:", aantalVerwerkt - aantalFout)
print("Aantal onjuiste kentekens:", aantalFout)
# sluit de drie bestanden
rdwInput.close()
scanInput.close()
signaleringen.close()

print("= = =  programma kentekensignalering afgesloten = = =")

# OPDRACHT
#
# Druk de huidige datum en tijd af
current_datetime = datetime.now()
print("Huidige datum:", current_datetime.date())
print("Huidige tijd:", current_datetime.time())