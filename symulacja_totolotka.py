from random import randrange

computer_list = [randrange(1,50) for i in range(6)]
print("wylosowane: \n",computer_list)

human_list = []
for i in range(6):
    liczba = int(input("Komputer wylosowal 6 liczb miedzy 1 a 49, zgadnij jakie to liczby :)Podaj 6 swoich liczb: "))
    human_list.append(liczba)

trafione = []
for item in human_list:
    if item in computer_list:
        trafione.append(item)

print(f"Ilosc zgadnietych liczb to: {len(trafione)}. Zgadłeś następujące liczby: ",trafione)
print(f"Liczby wylosowane przez komputer to: {computer_list}")