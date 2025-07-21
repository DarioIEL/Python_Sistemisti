# Il ciclo for fa parte della famiglia degli iteratori finiti
frutta = ["mela", "pera", "mango", "ciliegia"] 

for fr in frutta:
    print(f"Mangio", fr)
    
nomi = ["Fatima", "Viorel", "Magdy", "Gabri", "Cristian"]

for nome in nomi:
    print(f"Ciao",nome)
    
# For con un range di numeri
for numero in range(5):
    print(f"Numero", numero)
    
# For con un range e start e stop
print("---------Range da 10 a 20 con step 2--------")
for numero in range (10, 22, 2):
    print(f"Numero", numero)
    
# For con ENUMERATE, il quale crea una mappa chiave-valore
print("---Enumerate---")
colori = ["Giallo", "Rosso", "Nero", "Viola", "Azzurro", "Verde"]

for indice, colore in enumerate(colori):
    print(f"Colore {indice} valore {colore}")


