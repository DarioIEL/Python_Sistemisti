# ARRAY o LIST: sono dei contenitori di elementi simili tra loro, cioè dello stesso tipo, ordinati e 0-based

# Creao un array vuoto
miaLista = []

# Creo un array di elementi
frutta = ["mela", "pera", "mango", "ciliegia"]  # sono tutte string
numeri = [4, 7, 10, 0.5, 8.88]
misto = [1, True, "ciao", "dario", 36, False]

# Gli array fanno partte della macrofamiglia degli Enumerables, cioè ogni elemento dell'array ha un suo indice. L'indice parte da 0
#            0         1       2        3      4 
colori = ["Rosso", "Giallo", "Rosa", "Nero", "Blu"]

# Gli indici mi servono per poter "leggere", "accedere" alla lista in una determinata posizione, il corrispettivo valore
print(colori[0]) # Rosso
print(colori[3]) # Nero
print(frutta[1], colori[0]) # pera

# Aggiungo un elemento ad un array già costruito
colori.append("Verde")
print(colori)

frutta.append("Fragola")
print(frutta)

# Modificare un elemento in una data posizione
colori[0] = "Viola"
print(colori)

# Conto quanti elementi sono presenti nell'array
print(colori.__len__())
print(len(colori)) #length

# Eliminare un elemento in base al suo valore
colori.remove("Verde")
print(colori)

# Eliminare un elemento in base al suo indice
del colori[3]
print(colori)

# Voglio conoscere il valore dell'ultimo elemento
frutta.append("Melone")
print(frutta[len(frutta) - 1])