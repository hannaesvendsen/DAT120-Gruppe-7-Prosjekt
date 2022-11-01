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
        tittel1, sted1, startpunkt1, varighet1 = input("Skriv inn detaljene til avtalen ").split()
        print("Tittelen er {},sted er {}, startpunkt er {} og varighet i minutter er {} for avtalen".format(tittel1, sted1, startpunkt1, varighet1))
        print()
        
        
    


  
avtale_1 = avtale('Markus', 'Madla',x.strftime("%B") ,20)
avtale_2 = avtale('Nora', 'Storhaug',x.strftime("%B") ,30)
