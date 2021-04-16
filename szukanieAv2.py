tekst = "Ala ma kota, Alabama" #8

for i in enumerate(tekst):
    if i[1] == 'a' or i[1] == 'A':
        print(i[0])