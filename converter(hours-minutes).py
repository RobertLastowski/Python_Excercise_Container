def konwerter():
    wybor = input("Jezeli chcesz zamienic godziny na minuty wpisz \"g\" jezeli na odwrot wpisz \"m\"")
    if(wybor == "g"):
        ilosc = float(input(f"Podaj ilosc godzin: "))
        print(f"{ilosc} godzin to {ilosc * 60} minut")
    elif(wybor == "m"):
        ilosc = float(input(f"Podaj ilosc minut: "))
        print(f"{ilosc} minut to {round(ilosc / 60,3)} godzin")

#konwerter()