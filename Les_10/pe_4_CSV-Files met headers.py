import csv

def fmaken():
    bestand = 'index.csv'
    file = open(bestand, 'w', newline='')
    writer = csv.writer(file)

    writer.writerow(['Artikelnummer', 'Artikelcode', 'Naam', 'Voorraad', 'Prijs'])
    writer.writerow([121, 'ABC123', 'Highlight pen', 231, 0.56])
    writer.writerow([123, 'PQR678', 'Nietmachine', 587, 9.99])
    writer.writerow([128, 'ZYX163', 'Bureaulamp', 34, 19.95])
    writer.writerow([137, 'MLK709', 'Monitorstandaard', 66, 32.50])
    writer.writerow([271, 'TRS665', 'Ipad hoes', 155, 19.01])


def
fmaken()
