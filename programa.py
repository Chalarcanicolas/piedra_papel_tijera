# Piedra, papel o tijera

import random

print("--------------------------------------------")
print("-----------Piedra_papel o tijera-----------")
print("--------------------------------------------")

print("1 es piedra")
print("2 es papel")
print("3 es tijera")

# input

j = int(input("Digite la opción: "))
    
# processing

m = random.randint(1,3)

if (j == 1):
    if (m == 1 ):
        print("Empate")
    elif (m==2):
        print("Perdiste")
    else:
        print("Ganaste")

if (j == 2):
    if (m == 1):
        print("Ganaste")
    elif (m == 2):
        print("Empate")
    else:
        print ("Empate")
    

if (j == 3):
    if ( m == 1):
        print ("Perdiste")
    elif ( m ==2):
        print("Ganaste")
    else:
        print("Empate")
    