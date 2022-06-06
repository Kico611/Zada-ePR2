
from csv import reader

with open('rezultati.csv', 'r', encoding="utf8") as read_obj:
    csv_reader = reader(read_obj)
    studenti = list(map(tuple, csv_reader))
print("Polozili su:")
for ime, prezime, bodovi in studenti:
    if int(bodovi) > 49:
        print(ime, prezime)
studenti.sort(key=lambda y: y[1])
print(studenti)
dnevnik = {}
for ime,prezime,bodovi in studenti:
    if int(bodovi) < 50:
        dnevnik[ime,prezime] = "nedovoljan"
    if int(bodovi) >=50 and int(bodovi) < 65:
        dnevnik[ime,prezime] = "dovoljan"
    if int(bodovi) >=65 and int(bodovi) < 80:
        dnevnik[ime,prezime] = "dobar"
    if int(bodovi) >=80 and int(bodovi) < 90:
        dnevnik[ime,prezime] = "vrlo dobar"
    if int(bodovi) >=90:
        dnevnik[ime,prezime] = "odlican"
print(dnevnik)

