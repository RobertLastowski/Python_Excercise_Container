from random import randrange
ukryta = randrange(100)

while True:
    liczba = int(input("Komputer wylosowal liczbe miedzy 1 a 100, zgadnij jaka to liczba: "))
    if liczba > ukryta:
        print("Za dużo!")
    elif liczba < ukryta:
        print("Za mało!")
    elif liczba == ukryta:
        print("BRRAWO ZGADŁEŚ!")
        wybor = input("Chcesz zgadywac dalej?: ")
        if wybor == "tak":
            ukryta = randrange(100)
            print("Nowa liczba wylosowana, zaczynamy od poczatku :)")
        else:
            break