# -*- coding: utf-8 -*-
"""
Prosjektoppgave: Enkel avtalebok 
Dere skal implementere en enkel tekstbasert avtalebok, inkludert mulighet
 for å lagre avtalelista til fil 
og hente den fra fil. Avtaleboka skal kunne registrere avtaler med tittel,
 sted, start-tidspunkt og 
varighet 
"""
    
import datetime as dt

#d
class Avtale:
  def __init__(self, tittel, sted, start, varighet):
    self.tittel = tittel
    self.sted = sted
    self.start = start
    self.varighet = varighet
    
#e    
  def __str__(self):
    return f"tittel: {self.tittel}, Sted: {self.sted}, starttidspunkt: {self.start}, Varighet: {self.varighet}min" 

#f
def ny_avtale():
    Avtalen = None
    while not Avtalen:
        try:        
            tittel_1 = input("Angi tittel til avtalen : ")
            sted_1 = input("Angi stedet til avtalen : ")
            start_tidspunkt_1 = input("Angi dato og tidspunkt på formatet: dd:mm:yyyy tt:mm ")
            start_tidspunktdaytime = dt.datetime.strptime(start_tidspunkt_1, "%d:%m:%Y %H:%M")
            varighet_1 = int(input("Angi varighte i minutter :"))
            Avtalen=Avtale(tittel_1, sted_1, start_tidspunktdaytime, varighet_1)
        except Exception as error:
                print(error)
    return Avtalen
    
     
a=ny_avtale()
print (a)
      
#g      
def avtale_funksjon(ordliste, overskrift=""):
    print(overskrift)
    indeks = 1
    for avtale in ordliste:
        print(f"{indeks}: {avtale}")
        indeks += 1
      
avtaler_liste = list()

A1 = Avtale("Møte", "Stavanger", "placeholder", 30)



A2 = Avtale("Fotball", "Drammen", "placeholder", 90)



avtaler_liste.append(A1)
avtaler_liste.append(A2)



#avtale_funksjon(avtaler_liste)
avtale_funksjon(avtaler_liste, "Avtaler")


#h

def setteLista_ifilen ():
    avtale_lista_1 = ['Malin', 'Oslo', 'dd:mm:yyyy tt:mm', '120']
    tekstfil = open("Avtalene.txt", "w")
    for element in avtale_lista_1:
        tekstfil.write(element + "\n")
        tekstfil.close()
#j
printUtlista = []

def åpnefilen():
# åpne filen og les innholdet i en liste
    with open(r'Avtalene.txt', 'r') as fp:
        for line in fp:
        # fjerne linebreak fra et nåværende navn
        # linebreak er det siste tegnet i hver linje
            x = line[:-1]

        # legge til gjeldende element i listen
            printUtlista.append(x)

    print(printUtlista)
       
#l

def menu ():
    print("[1] Lese inn avtale.")
    print("[2] Skrive inn avtale til fil.")
    print("[3] Skrive inn ny avtale")
    print("[4] Skrive ut alle avtaler.")
    print("[5] Avslutte programmet")

    print("Du må ta valgene til venstre for å velge et alternativ")

menu()
option = int(input("Skriv inn ditt alternatv:"))

while option !=0:
    if option == 1:
        print("Du har valgt alternativ 1 - (Lese inn avtale)")
    elif option == 2:
        print("Du har valgt alternativ 2 - (Skrive inn avtale til fil)")
    elif option == 3:
        print("Du har vlagt alternativ 3 - (Skrive inn ny avtale)")
    elif option == 4:
        print("Du har valgt alternativ 4 - (Avslutte programemt)")

print()
menu()
option = int(input("Skriv inn ditt alternativ"))
