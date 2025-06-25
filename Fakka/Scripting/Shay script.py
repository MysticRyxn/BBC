# programma KentekenCheck
# Versie: 1.2
# Auteur: B. van der Feen
# Edit: M. van Hoek
# Datum:  14/7/2022

from datetime import datetime

# OPDRACHT
# Maak de variabele appPath aan en gebruik die om op één plek om het pad te definieren voor alle bestanden.
appPath = "C:\\Users\\administrator\\KentekenCheck\\"

print("= = =  programma kentekensignalering gestart = = = ") 

# OPDRACHT
# Druk de huidige datum en tijd af
current_datetime = datetime.now()
print("Huidige datum:", current_datetime.date())
print("Huidige tijd:", current_datetime.time())

# Open de invoerbestanden met gebruik van appPath
rdwInput = open(appPath + "RDW.csv")
scanInput = open(appPath + "GescandeData.csv")
aantalVerwerkt = aantalFout = 0

# OPDRACHT
# Vraag hier of het bestand vals.txt leeg gemaakt moet worden (j of n)
legenVals = input("Wil je het bestand vals.txt leegmaken? (j of n): ").lower()

# Bestand vals.txt openen op basis van keuze
if legenVals == "j":
    signaleringen = open(appPath + "vals.txt", "w")
    print("Het bestand vals.txt is leeggemaakt.")
elif legenVals == "n":
    signaleringen = open(appPath + "vals.txt", "a")
    print("Het bestand vals.txt wordt niet leeggemaakt.")
else:
    print("Ongeldige keuze. Bestand wordt niet leeggemaakt.")
    signaleringen = open(appPath + "vals.txt", "a")

# Verwerking gescande kentekens
for auto in scanInput:
    if len(auto) < 10:
        continue
    autoDelen = auto.strip().split(",")
    scanKenteken = autoDelen[0]
    scanMerk = autoDelen[1]
    scanType = autoDelen[2]
    aantalVerwerkt += 1

    match = 0
    rdwInput.seek(0)
    for rdwAuto in rdwInput:
        rdwAutoDelen = rdwAuto.strip().split(",")
        rdwKenteken = rdwAutoDelen[0]
        rdwMerk = rdwAutoDelen[2]
        rdwType = rdwAutoDelen[3]

        # OPDRACHT
        # Als kentekens overeenkomen, dan wordt match op 1 gezet en moet gestopt worden met zoeken
        if scanKenteken == rdwKenteken:
            match = 1
            break

    if match == 0:
        aantalFout += 1
        print("Onbekend kenteken:", scanKenteken, scanMerk, scanType, "\n")
        signaleringen.write("Onbekend," + scanKenteken + "," + scanMerk + "," + scanType + "\n")
    else:
        if scanMerk != rdwMerk or scanType != rdwType:
            aantalFout += 1
            print("Onjuist kenteken:", scanKenteken, scanMerk, scanType)
            print("Geregistreerd op:", rdwKenteken, rdwMerk, rdwType, "\n")
            signaleringen.write("Onjuist," + scanKenteken + "," + scanMerk + "," + scanType + "\n")

# OPDRACHT
# print het aantal correcte kentekens en print het aantal onjuiste kentekens
print("Eindtotalen KentekenCheck")
print("Aantal correcte kentekens:", aantalVerwerkt - aantalFout)
print("Aantal onjuiste kentekens:", aantalFout)

# Sluit de bestanden
rdwInput.close()
scanInput.close()
signaleringen.close()

# OPDRACHT
# Druk de huidige datum en tijd af
current_datetime = datetime.now()
print("Einde datum:", current_datetime.date())
print("Einde tijd:", current_datetime.time())

print("= = =  programma kentekensignalering afgesloten = = =")
