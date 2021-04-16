import random

liczba = random.randint(1, 10)
proby = 3

for i in range(proby):
    print("Próba", i+1)
    odp = input("Twoja liczba: ")
    if liczba == int(odp):
        print("Brawo!")
        break
    elif i == proby-1:
        print("Przegrałeś :(")
    else:
        if int(odp) > liczba:
            print("Wylosowana liczba jest mniejsza\n")
        else:
            print("Wylosowana liczba jest większa\n")
