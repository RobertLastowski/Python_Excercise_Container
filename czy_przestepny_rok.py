'''
FUNKCJA SPRAWDZAJĄCA CZY ROK JEST PRZESTĘPNY
'''
def przestepny(rok):
    if (rok % 4 == 0 and rok % 100 != 0) or rok % 400 == 0:
        return True
    else:
        return False
'''
FUNKCJA SPRAWDZAJĄCA ILE DNI BYŁO W DANYM MIESIACU I DANYM ROKU
'''
def ile_dni(miesiac, czy_przestepny):
    if miesiac == 2:
        if czy_przestepny == True:
            return 29

        return 28

    if miesiac > 7:
        if miesiac % 2 == 0:
            return 31
        else:
            return 30

    else:
        if miesiac % 2 == 0:
            return 30
        else:
            return 31

'''
FUNKCJA SPRAWDZAJĄCA KTRÓYM DNIEM ROKU BYŁ DZIEŃ Z PODANEJ DATY
'''
def ktory_dzien(rok,miesiac,dzien):
    #najpierw walidacja daty
    suma = dzien
    if dzien > ile_dni(miesiac,przestepny(rok)) or miesiac > 12 or miesiac <1:
        return None
    else:
        for i in range(1,miesiac):
            print(suma)
            suma += ile_dni(i,przestepny(rok))
        return suma

print(ktory_dzien(2020,12,31))


'''
FUNKCJA ZAIMPLEMENTOWANA W WERSJI Z NAZWAMI MIESIECY SŁOWNIE
'''
# def miesiace(miesiac,czy_przestepny):
#     if miesiac.lower() == "styczeń" or miesiac.lower == "marzec" or miesiac.lower == "maj" or miesiac.lower == "lipiec" or miesiac.lower == "sierpien" or miesiac.lower == "październik" or miesiac.lower == "grudzień":
#         return 31
#     elif miesiac.lower() == "kwiecień" or miesiac.lower() == "czerwiec" or miesiac.lower() == "wrzesien" or miesiac.lower() == "listopad":
#         return 30
#     elif miesiac.lower() == "luty":
#         if czy_przestepny == True:
#             return 29
#         else:
#             return 28
#     else:
#         print("Nie ma takiego miesiaca :c użyj prosze polskich znaków :)")

# rok = int(input("Podaj rok a powiem Ci czy jest przestepny: "))
# print(przestepny(rok))
# miesiac = input("Podaj mieisac a powiem ile mial dni w tym roku: ")
# print(miesiace(miesiac,przestepny(rok)))