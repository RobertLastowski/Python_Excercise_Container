def stosunek(a,b):
    if a > b:
        print(f"Liczba a = {a} jest wieksza od liczby b={b}")
    elif a < b:
        print(f"Liczba a = {a} jest mniejsza od liczby b={b}")
    else:
        print(f"Liczba a = {a} jest rowna liczbie b={b}")

while True:
    print("To jest porownywarka liczb")
    a = float(input("Podaj pierwsza liczbe: "))
    b = float(input("Podaj druga liczbe: "))
    stosunek(a,b)
    
    wybor = input("Chcesz porownywac dalej? Wpisz tak lub nie: ")
    if wybor == "tak":
        continue
    elif wybor == "nie":
        break
