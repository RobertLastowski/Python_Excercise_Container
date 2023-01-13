'''
Ćwiczenia z klas i dziedziczenia
'''

class Person():
    def __init__(self,imie,naziwsko,wiek,płeć):
        self.imie = imie
        self.nazwisko = naziwsko
        self.wiek = wiek
        self.płeć = płeć

    def __str__(self):
        return "Imie: " + self.imie + "\nNaziwsko: " + self.nazwisko + "\nWiek: " + str(self.wiek) + "\nPłeć: " + self.płeć

class Student(Person):
    def __init__(self,imie,naziwsko,wiek,płeć,oceny = []):
        self.oceny = oceny
        super().__init__(imie,naziwsko,wiek,płeć)

    def srednia(self):
        suma = 0
        for item in oceny:
            suma += item
        return suma/len(oceny)

    def __str__(self):
        s = super().__str__()
        return "Stduent:\n" + s + "\nOceny: " + str(self.oceny) + "\nŚrednia: " + str(self.srednia())

class Employee(Person):
    def __init__(self,imie,naziwsko,wiek,płeć,zarobki):
        self.zarobki = zarobki
        super().__init__(imie,naziwsko,wiek,płeć)

    def __str__(self):
        s = super().__str__()
        return "Pracownik:\n" + s + "\nZarobki: " + str(self.zarobki)

#Tworzenie instancji klas
oceny = [5,5,4,2]
student1 = Student("Robert","Łastowski",24,"M",oceny)
pracownik1 = Employee("Tomek","Kiełbasa",26,"M",15000)
student2 = Student("Grażka","Łopata",55,"K",oceny)

#Filotrowanie listy osób ze względu na płeć
lista_osob = [student1,pracownik1,student2]
for i in filter(lambda p: p.płeć =="M", lista_osob):
    print (i)

#Filotrowanie listy osób z warunkiem "czy student"
studenci = list(filter(lambda p : isinstance(p,Student),lista_osob))
print("Studenci:",studenci)

