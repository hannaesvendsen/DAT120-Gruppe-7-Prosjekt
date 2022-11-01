# -*- coding: utf-8 -*-
"""
Prosjektoppgave: Enkel avtalebok 
Dere skal implementere en enkel tekstbasert avtalebok, inkludert mulighet
 for å lagre avtalelista til fil 
og hente den fra fil. Avtaleboka skal kunne registrere avtaler med tittel,
 sted, start-tidspunkt og 
varighet 
"""

from datetime import datetime

x = datetime.datetime(2022, 1, 11)
class avtale:
    
    def __init__(self, tittel, sted, startTidspunkt, varighet):
        self.tittel = tittel
        self.sted = sted
        self.startTidspunkt = startTidspunkt
        self.varighet = varighet

    def __str__(self):
        return f'tittel {self.tittel}, sted {self.sted},starttidspunkt {self.startTidspunkt}, varighet {self.varighet}'
        
    def ny_avtale(self):
        try:
            lst = []  
            n = int(input("Skriv inn avtalen(tittel, sted, startpunkt og varighet i minutter) : "))

            for i in range(0, n):
                ele = int(input())
            lst.append(ele) 
            print(lst)     
        except ValueError:
            try:               
                n = float(input)
                print("ditt input er ikke gyldig prøv på nytt. Du skrev =", n)
            
    

       
avtale_1 = avtale('Markus', 'Madla',x.strftime("%B") ,20)
avtale_2 = avtale('Nora', 'Storhaug',x.strftime("%B") ,30)
