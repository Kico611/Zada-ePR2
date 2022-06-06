import random
br1 = br2 = br3 = br4 = br5 = br0 = 0
imena = ['Josip', 'Ivan', 'Ivan', 'Josip', 'Ivan', 'Ivan', 'Katarina', 'Božena', 'Ivona', 'Marija', 'Josipa', 'Marko', 'Dario', 'Mihael',
'Stana', 'Bruno', 'Anamarija', 'Andrea', 'Petar', 'Marko', 'Amnesa', 'Nikola', 'Antonela', 'Leon', 'Ivan', 'Ante', 'Ivan',
'Jure', 'Jan', 'Florijan', 'Boris', 'Ivan', 'Stipe', 'Damir', 'Ana', 'Tin', 'Iva', 'Kristina', 'Josip', 'Tomislav', 'Luka', 'Ivan',
'Martin', 'Marko', 'Ante', 'Nikolina', 'Ivan', 'Toni', 'Ante', 'Darija', 'Dominik', 'Lucija', 'Luka', 'Ana', 'Emanuel',
'Petar', 'Matej', 'Stjepan', 'Josip', 'Luka', 'Marija', 'Toni', 'Iva ', 'Perica', 'Antonio', 'Ante', 'Marijan', 'Mario',
'Antonio', 'Stipe', 'Filip', 'Ivan', 'Ivan', 'Luka', 'Ante Bruno', 'Ivan', 'Vinko', 'Ivan', 'Matijas', 'Ivan', 'Freda', 'Kristina',
'Josip', 'Lucija']
dnevnik = {}
for ime in imena:
          dnevnik[ime] = random.randint(1,5)
for ime in dnevnik:
    br0 += 1
    if dnevnik[ime] == 1:
        br1 +=1
    elif dnevnik[ime] == 2:
        br2 +=1
    elif dnevnik[ime] == 3:
        br3 +=1
    elif dnevnik[ime] == 4:
        br4 +=1
    elif dnevnik[ime] == 5:
        br5 +=1
print(dnevnik)
postotak = ((br2+br3+br4+br5)/br0) * 100
print("Broj ucenika koji su prosli s 1: ",br1)   
print("Broj ucenika koji su prosli s 2: ",br2)
print("Broj ucenika koji su prosli s 3: ",br3)
print("Broj ucenika koji su prosli s 4: ",br4)
print("Broj ucenika koji su prosli s 5: ",br5)
print("Postotak prolaznosti je: ",postotak,"%")
