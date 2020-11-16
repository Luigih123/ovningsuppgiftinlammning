mål = int(input('Ange ett heltal antal kroner som är ditt mål: ')) #Användaren skriver ett mål, alltså antal pengar den vill nå
mål = mål*100 #Konverterar öre till kronor
öre = 1 #Startvärde för öre
dagar = 0 #Starvärde för dagar
while öre <= mål: #Loopar programet tills öre är lika mycket eller mer än målet
    dagar = dagar + 1 #Varje gång programent gör en loop så lägger den till 1 dag på antal dagar
    öre = öre*2 #Lönen dubblas varje gång den gör en loop
print(f'Det tog {dagar} dagar tills du uppnådde ditt mål på {mål/100:.0f} kr! ') #Den skriver ut hur många dagar det tog och hur mycket pengar du fick
