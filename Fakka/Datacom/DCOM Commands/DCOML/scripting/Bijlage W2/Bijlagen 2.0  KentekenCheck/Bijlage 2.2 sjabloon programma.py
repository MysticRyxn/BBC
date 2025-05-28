# programma KentekenCheck
# Versie: 1.2
# Auteur: B. van der Feen
# Edit: M. van Hoek
# Datum:  14/7/2022
#
#

from datetime import datetime

# OPDRACHT
#
# Maak de variabele appPath aan en gebruik die om op één plek om het pad te definieren voor alle bestanden.
# Gebruik vervolgens appPath overal bij het verwijzen naar het pad van de bestanden.
# Doe dit voor eventuele nieuwe verwijzingen én vervang de bestaande verwijzingen in deze code.

print("= = =  programma kentekensignalering gestart = = = ") 

# OPDRACHT
#Druk de huidige datum en tijd af

# deze code laat de current time en current day zien wanneer het script word gerunned 
import datetime

Get current_date and time
current_datetime = datetime.datetime.now()

Extract the date and time components
current_date = current_datetime.date()
current_time = current_datetime.time()

Print the date and time
print("Current Date:", current_date)
print("Current Time:", current_time)

rdwInput = open("C:\\Users\\administrator\\KentekenCheck\\RDW.csv")
scanInput = open("C:\\Users\\administrator\\KentekenCheck\\GescandeData.csv")
aantalVerwerkt = aantalFout = 0
legenVals = ""

# OPDRACHT
#
# Vraag hier of het bestand vals.txt leeg gemaakt moet worden (j of n)
# Sla de keuze op in de variabele legenVals

# In deze code laat ik zien dat bij het bestand vals.txt op de gebruiker de inhoud wilt verwijderen waarop hub ja of nee moeten zeggen  

keuze = input("Wil je het bestand vals.txt leegmaken? (j of n): ")

if keuze.lower() == "j":
    # Code om het bestand vals.txt leeg te maken
    with open("vals.txt", "w") as f:
        f.write("")
        print("Het bestand vals.txt is leeggemaakt.")
elif keuze.lower() == "n":
    print("Het bestand vals.txt wordt niet leeggemaakt.")
else:
    print("Ongeldige keuze.")
    
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
        # en moet gestopt worden met zoeken in RDW.txt
        
        # deze code checkt de kentekens of ze overeenkomen zo ja dan word match op 1 gezet en stopt het met zoeken in RDW.txt
        def zoek_kenteken(kenteken):
                match = 0

    with open("RDW.txt", "r") as file:
        for line in file:
            if kenteken in line:
                match = 1
                break

            return match     

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
# print het aantal correcte kentekens en print het aantal onjuiste kentekens
# sluit de drie bestanden

# deze code laat het aantal correcte kentekens en aantal onjuiste kentekens en sluit de 3 bestanden 
def count_kentekens():
   
    correct_count = 0
    incorrect_count = 0

    with open("RDW.txt", "r") as rdw_file, open("correct.txt", "r") as correct_file, open("onjuist.txt", "r") as incorrect_file:
        for line in rdw_file:
            correct_count += 1

        for line in correct_file:
            correct_count += 1

        for line in incorrect_file:
            incorrect_count += 1

    return correct_count, incorrect_count



print("= = =  programma kentekensignalering afgesloten = = =")

# OPDRACHT
#
# Druk de huidige datum en tijd af
# deze code laat de current time en current day zien wanneer het script word gerunned 
import datetime

current date and time
current_datetime = datetime.datetime.now()

Extract the date and time components
current_date = current_datetime.date()
current_time = current_datetime.time()

Print the date and time
print("Current Date:", current_date)
print("Current Time:", current_time)
