import math
# Le funzioni sono blocchi di codice wrappato e riutilizzabile a comando. Questo mi permette di rendere il codice più flessible e modulare

# Struttura di base
def nome_funz(params):
    # Corpo della funzione
    nomeUser = "Dario"
    print(nomeUser)
    return params

# return mi restituisce in uscita un valore
# params prende in ingresso dei valori
# ATT: i parametri (params) così come return non sono obbligatori

# Definisco la funzione
def saluta():
    print("ciao sistemisti")


# Per poter eseguire la funzione devo per forza richiamarla
saluta()

# Definisco una funzione con i parametri
def saluta_user(nomeUser):
    print(f"Ciao {nomeUser}, benvenuto in aula !")

saluta_user("Mario")

# Posso anche passare più parametri alla stessa funzione
def somma(a, b, c):
    risultato = a + b + c
    return float(risultato)

x = somma(1, 2, 3) # in questo caso sto raccogliendo il valore restituito
print("Il risultato è", x)

# Funzione con più valori di return 
def calc_area_perim(base, altezza):
    area = base * altezza
    perimetro = (base + altezza) * 2

    return area, perimetro

# print("L'area e il perimetro valgono",calc_are_perim(6, 5))
# RICORDA: nel caso in cui ho più valori restiuiti devo andare ad istanziare tante variabili quanti sono i valori restituiti
a, p = calc_area_perim(6,5)
print(f"L'area vale: {a}, il perimetro vale {p}")

# Funzioni con parametri Predefiniti. In questo caso, il valore di default dell'età è 25
def presenta_persona(nome, eta = 25):
    return f"Ciao mi chiamo {nome} e ho {eta} anni"

print(presenta_persona("Anna"))
print(presenta_persona("Marco", 30))


# Funzione con una array come parametro
def calcola_media(numeri):
    if len(numeri) == 0:
        return 0
    else:
        return sum(numeri) / len(numeri)

voti = [25, 30, 20, 19, 27, 30]
media = calcola_media(voti)
print(f"La media dei voti degli esami è: {round(media)}")
        

# Esempio funzioni ricorsive, cioè funzioni che chiamano se stesse
def fattoriale(n):
    if n < 1:
        return 1
    return n * fattoriale(n - 1)

print( fattoriale(5) )

# Le funzioni possono richiamare ed essere rtichiamate da altre funzioni
def prima_funz(saluto):
    return saluto

def seconda_funz(nome):
    return nome

def terza_funz(cognome):
    return cognome

def esegui_all():
    saluto = prima_funz("Ciao")
    nome = seconda_funz("Dario")
    cognome = terza_funz("Mennillo")
    return saluto + " " + nome + " " + cognome

print(esegui_all())