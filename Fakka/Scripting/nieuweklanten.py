import csv

bestandNieuw = "Klanten-nieuw.csv"
bestandOud = "Klanten-oud.csv"

klantenNieuw = []
klantenOud = []

with open(bestandNieuw, 'r') as klantenNieuwObj:
    klantenObjCsv = csv.reader(klantenNieuwObj,delimiter=';')
    headerNieuw = next(klantenObjCsv)
    for rij in klantenObjCsv:
        klantenNieuw.append(rij)

with open(bestandOud, 'r') as klantenOudObj:
    klantenOudObjCsv = csv.reader(klantenOudObj,delimiter=';')
    headerOud = next(klantenOudObjCsv)
    for rij in klantenOudObjCsv:
        klantenOud.append(rij)

for line in klantenNieuw:
    for lineOud in klantenOud:
        if line[6] == lineOud[6]:
            # print(f"{line} is een bestaande klant")	
            break
    else:
        print(f"{line} is een nieuwe klant")

