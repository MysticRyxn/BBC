import csv # Hier importeer ik de csv bestanden.

from datetime import datetime # Hierdoor kan ik de huidige datum printen.

actuele_tijd = datetime.now()
tijd = actuele_tijd.strftime("%Y-%m-%d %H:%M:%S") # Hier heb ik een variabele aangemaakt zodat de tijd word weergeven als je het programma start.

print("= = = programma kentekensignalering gestart = = =", tijd ) # Hier krijg je te zien dat het programma gestart is en wat de huige tijd is.


# Hier vraag ik of het bestand vals.txt leeg gemaakt moet worden.
while True:
    vals_leeg = input("Wil je het bestand vals.txt leegmaken? (j of n): ")

    if vals_leeg == 'j':
        with open("vals.txt", "w") as leeg:
            print("Het bestand vals.txt is leeggemaakt.\n")
        break  # Hier verlaat je de loop nadat je 'j' hebt ingevoerd.

    elif vals_leeg == 'n':
        print("Het bestand vals.txt wordt niet leeggemaakt.\n")
        break  # Hier verlaat je de loop nadat je 'n' hebt ingevoerd.

    else:
        print("Ongeldige invoer. Voer alstublieft 'j' of 'n' in.") # Je blijft in de loop als je niks invoert



vals = open("vals.txt", "a" if vals_leeg == 'n' else "w") # Het bestand vals.txt wordt in append- of write-modus geopend, 
#afhankelijk van de gebruikerskeuze in vals_leeg, waarbij 'a' data toevoegt zonder te wissen en 'w' bestaande inhoud wist voordat nieuwe data wordt toegevoegd.


aantal_kentekens = fout_kentekens = 0 # Beide waardes worden opgeslagen als 0.

# Hier wordt het bestand 'GescandeData.csv' geopend in leesmodus.
with open("GescandeData.csv", "r") as gescandeAuto:
    for auto in gescandeAuto:
        aantal_kentekens+=1
        if len(auto) < 5:  #Als de lengte van de regel minder dan 5 tekens is, ga verder met de volgende regel.
            continue

#Hier wordt de regel op de komma's gesplit en slaat autoDelen op in een lijst.
        autoDelen = auto.split(",")
        if len(autoDelen) < 3: #Als de lijst minder dan 3 delen bevat ga je verder met de volgende regel.
            continue

        Auto_kenteken, Auto_merk, Auto_handelsbenaming = autoDelen[0], autoDelen[1], autoDelen[2].strip()

        match = False

        with open("RDW.csv", "r") as RDW:
            for RDW_auto in RDW:
                rdwAuto = RDW_auto.split(",")
                if len(rdwAuto) < 4:
                    continue

                RDW_kenteken, RDW_merk, RDW_handelsbenaming = rdwAuto[0], rdwAuto[2], rdwAuto[3].strip()
                if Auto_kenteken == RDW_kenteken:
                    match = True
                    break

        if not match:
            print(f"Onbekend kenteken: {Auto_kenteken}, {Auto_merk}, {Auto_handelsbenaming}")
            vals.write(f"Onbekend,{Auto_kenteken},{Auto_merk},{Auto_handelsbenaming}\n")

        else:
            if Auto_merk != RDW_merk or Auto_handelsbenaming != RDW_handelsbenaming:
                fout_kentekens += 1
                print(f"Onjuist kenteken: {Auto_kenteken}, {Auto_merk}, {Auto_handelsbenaming}")
                print(f"Geregistreerd op: {RDW_kenteken}, {RDW_merk}, {RDW_handelsbenaming}")
                vals.write(f"Onjuist,{Auto_kenteken},{Auto_merk},{Auto_handelsbenaming}\n")

vals.close()

print("\nEindtotalen KentekenCheck:")
print(f"Aantal correcte kentekens: {aantal_kentekens}\n",f"aantal onjuiste kentekens: {fout_kentekens}\n")

print(f"= = = programma kentekensignalering afgesloten = = =", tijd)