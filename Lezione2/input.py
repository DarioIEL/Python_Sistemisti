# Come prendere in ingresso un valore inserito dall'utente
import math


print("Ciao, inserisci il tuo nome") #output

nomeUser = input() # Questa è un'altra funzione built-in

print("Benvenuto in piattaforma,", nomeUser)

print("Inserisci il primo numero:")
# CAST del dato, forzare una variabile ad essere di un determinato tipo
# num1 = int(input())
num1 = math.trunc(float(input()))

print("Inserisci il secondo numero:")
# num2 = int(input())
num2 = float(input())

somma = num1 + num2
prod = num1 * num2
diff = num1 - num2
div = num1 / num2

print("I risultati sono:\n", somma, "\n", prod, "\n", diff, "\n", div)
