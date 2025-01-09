# Arbeidskrav 2 i PY1010-1 24H Grunnleggende programmering med Python
# Skrevet av: Nabil Safadi
# Beskrivelse: løsning på arbeidskrav 2 - 6 oppgaver i en fil

import numpy as np
from matplotlib import pyplot as plt

#Oppgave 1
alder = int(input('Hvilket år er du født? ') )
alder = 2024 - alder
print('Du er (eller blir i løpet av året)', alder, 'år gammel')

#Oppgave 2
antall_elever = int(input('Skriv inn antall elever:' ))
pizzastykke = 0.25
antall_pizzaer = antall_elever * pizzastykke
print('Antall pizzaer som trengs er:', f"{np.ceil(antall_pizzaer):.0f}")

#Oppgave 3
v_grad = float(input('Skriv inn gradtallet:' ))
v_rad = v_grad*np.pi/180 #samme som v_rad = np.radians(v_grad)
print('Gradtallet', v_grad, 'omregnes til radiantallet', format(v_rad, '.3f'))

#Oppgave 4
# Oppgave 4a
data = {
    "Norge": ["Oslo", 0.634],
    "England": ["London", 8.982],
    "Frankrike": ["Paris", 2.161],
    "Italia": ["Roma", 2.873]
}
# Oppgave 4b
brukerinput = input("Skriv inn landet du vil lære om: ")
landinfo = data[brukerinput]
print(f"{landinfo[0]} er hovedstaden i {brukerinput} og "
      f"det er {landinfo[1]} mill. innbyggere i {landinfo[0]}")
# Oppgave 4c
nyttland = input("Skriv inn det nye landet du vil legge til: ")
nyttlandhovedstad = input(f"Skriv inn hovedstaden til {nyttland}: ")
nyhovedstadbefolkning = input(f"Skriv inn antall innbyggere i hovedstaden {nyttlandhovedstad}: ")
data[nyttland] = [nyttlandhovedstad, nyhovedstadbefolkning]
print("Alle data i dictionary", data)

#Oppgave 5
lillekatet_diameter = float(input('Skriv inn lengde på a: '))
storekatet = float(input('Skriv inn lengde på b: '))
# Trekanten
hypotenus = np.sqrt(lillekatet_diameter**2 + storekatet**2)
areal_trekant = 1/2 * lillekatet_diameter * storekatet
omkrets_trekant_uten_lillekatet = storekatet + hypotenus
#Sirkelen
radius = lillekatet_diameter/2
areal_halvsirkel = (np.pi * (radius)**2)/2
omkrets_sirkel_halv = (2 * np.pi * radius) - lillekatet_diameter
# Areal og omktrets av figuren
areal_figur = areal_trekant + areal_halvsirkel
omkrets_figur = omkrets_trekant_uten_lillekatet + omkrets_sirkel_halv
#Skriv ut resultatet
print('Arealet av figuren er', f'{areal_figur:.2f}','kvadratenheter',
      'og omkretsen av figuren er', f'{omkrets_figur:.2f}','lengdeenheter')

#Oppgave 6
def funksjon(x):
    y = -x**2 - 5
    return y

x = np.linspace(-10, 10, 200)
y= funksjon(x)

#Plotting
plt.close('all')
plt.figure(1, figsize=(12, 9))
plt.plot(x, y, label='f(x) = -x^2 - 5')
plt.xlabel('x-aksen')
plt.ylabel('f(x) (y-aksen)')
plt.legend()
plt.grid()
plt.savefig('Oppgave6.pdf')
plt.show()
