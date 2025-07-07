# 1. Le varibili sono un contenitore di un'informazione singola che cambia nel corso del codice
# 2. Denominazione: i nomi delle var devono essere "parlanti", ovvero descrittive
# 3. Non posso denominare una variabile con uno dei seguenti nomi: for, if, while, switch, super, true, false, assert ecc ecc
# 4. Posso utilizzare:
# camelCase  OK
# snake_case OK
# UPPERCASE (va bene per le costanti)
# kebab-case NO

# Dichiarare una variabile e assegnare un valore
# nomeVar = valore

nomeUtente = "Dario"
eta = 36
corsiAssegnati = 2
studenti = 40
studenti = studenti + 1
studenti += 1
studenti -= 1


# Richiamo, leggo una variabile
print(nomeUtente)


#Concateno più variabili
print("Ciao", nomeUtente, "hai", eta, "anni.", "Attualmente insegni in", corsiAssegnati, "corsi con un totale di", studenti, "studenti")

# Le varibili possono interagire anche tra loro

# Esempio: devo calcolare la media di un esame all'università
votoScritto = 30
votoOrale = 21

# voto finale è la media tra i due
votoFinale = (votoScritto + votoOrale) / 2
# Psso riassegnare una variabile, richiamandolo con lo stesso nome
votoFinale = 30

print("Voto esame:", votoFinale)

# Come definire delle COSTANTI. Per convenzione si usano nomi in MAIUSC
# In py non è esiste il concetto di costante vera e propria
PIGRECO = 3.14159
VELOCITA_LUCE = 300000 #m/s
MAX_STUDENTI = 30

MAX_STUDENTI = 40

print(MAX_STUDENTI)