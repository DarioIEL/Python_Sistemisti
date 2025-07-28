# Dato il seguente array determinare se il numero è pari o dispari

# Dato il seguente array di voti calcola la media

#Utilizzando l'array precedente stampa tutti i numeri, al primo multiplo di 25 esci dal ciclo (utilizza break)

#Utilizzando lo stesso array stampa tutti i numeri, salta il numero 100 (utilizza continue)

# Stampa i numeri da 1 a 100. Per tutti i numeri multipli di 3 stampa "ZOOM", per i tutti i multipli di 5 stampa "BOOM", per i multipli di entrambi stampa "ZOOM BOOM"

# Data la lista [2, 7, 1, 9, 3], trova il numero più grande

# Conta quante volte appare ogni vocale nella parola 'programmazione'


############## ES1 ##################
#Faccio scorrere il mio array e un numero alla volta controllo se pari o dispari
numeri = [6,7,22,34,6,8,9,11,27,87,75,4,42]
for numero in numeri:
    if numero % 2 == 0:   # 0 == 0 TRUE, 0 is equal to 0 ?
        print(numero, "pari")
    else:
        print(numero, "dispari")


############## ES2 ############## 
print("Esercizio media voto")
# Faccio scorrere l'array, sommo valore per valore e poi divido tutto per il numero di valori presenti
voti = [85, 66, 90, 100, 50, 92, 67]

totale = 0

for voto in voti:
    totale += voto
    # totale = totale + voto


media = totale / voti.__len__()

print(f"La media dei tuoi voti vale: {media:.2f}")

media2 = sum(voti) / len(voti);
print("La media dei tuoi voti vale: ", media2)

################## ES3 ##################
#Utilizzando l'array di voti al primo multiplo di 25 esce dal ciclo 
print("ES3")
#   variabile arbitraria, cioè
for voto in voti:
    if voto % 25 == 0:
        print("Questo è il primo multiplo di 25:", voto)
        print("Esco dal ciclo")
        break
    
########### ES4 ##############
#Utilizzando lo stesso array stampa tutti i numeri, salta il numero 100 (utilizza continue)

print("ES4")
for voto in voti:
    if voto == 100:
        print(f"Questo {voto} lo salto")
        continue
    print(voto)
    
    
########## ES5 ###############

# Stampa i numeri da 1 a 100. Per tutti i numeri multipli di 3 stampa "ZOOM", per i tutti i multipli di 5 stampa "BOOM", per i multipli di entrambi stampa "ZOOM BOOM"

print("******* ES5 **********")

# # Variabile globale
serieNumeri = range(1,101)

# Numero è una variabile locale, vive solo all'interno del ciclo for
for numero in serieNumeri:
    if numero % 3 == 0 and numero % 5 == 0:
        print(f"{numero} ZOOM BOOM")
    elif numero % 5 == 0:
        print(f"{numero} BOOM")
    elif numero % 3 == 0:
        print(f"{numero} ZOOM")
    else:
        print(numero)        


# # Ver2 
# for numero in range(1, 101):
#     output = ""
#     if numero % 3 == 0:
#         output += "ZOOM"
#     if numero % 5 == 0:
#         output += " BOOM" if output else "BOOM"
        
#     print(f"{numero}: {output}" if output else numero)


############### ES6 ################
# Data la lista [2, 7, 1, 9, 3], trova il numero più grande
print("ES6")

listaNumeri = [2, 7, 1, 9, 3, 5, 100]
# massimo = max(listaNumeri)
# print("Il valore massimo é", massimo)

# Faccio la stessa cosa utilizzando un ciclo for
massimo = listaNumeri[0]

for numero in listaNumeri:
    if numero > massimo:
        massimo = numero
        
print(f"Il valore massimo vale: {massimo}")


# voglio la lista ordinata di numeri 
listaOrdinata = sorted( listaNumeri, reverse=True) #Bubble Sort
print(listaOrdinata)

###################### ES 6 ##################
# Conta quante volte appare una vocale nella parola programmazione
print("ES 6")

# parola = "programmazione"
# vocali = ['a', 'e', 'i', 'o', 'u']

# lungParola = len(parola)
# print(f"Lunghezza parola {lungParola}")

# contaVocali = 0

# for vocale in vocali:
#     vocaleTrovata = parola.count(vocale)
#     print(f"Vocale {vocale} trovata {vocaleTrovata} volte")
    
# totaleVocali = sum(parola.count(v) for v in vocali)
# print(f"Vocali in totale: {totaleVocali}") 

parola = "programmazione"
vocali = ['a', 'e', 'i', 'o', 'u']

contatore = 0

for lettera in parola:
    # if lettera in vocali:
    #     contatore += 1
    for vocale in vocali:
        if lettera == vocale:
            print(f"Vocale trovata {lettera}")
            contatore+=1
         
    
print(f"Vocali in totale: {contatore}") 

