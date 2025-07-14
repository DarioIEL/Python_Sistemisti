# If STATEMENT. fa parte dei paradigmi fondamentali della programmazione ed è una struttura di controllo. Mi permette di valutare delle condizioni 

# Sintassi: if condizione:
#               codice da eseguire se condizione è True
#           else:
#               codice da eseguire se condizione è False

eta = 36

if eta >= 18:
    print("Sei maggiorenne. Hai", eta, "anni")
else:
    print("Sei minorenne. Hai", eta, "anni") 

# Posso "invertire" la logica
# if eta < 18:
#     print("Sei minorenne. Hai", eta, "anni") 
# else:
#     print("Sei maggiorenne. Hai", eta, "anni")

# Posso espandere la logica, andando a valutare più casi, utilizzando un elif (else if)
voto = 100

if voto >= 80:
    print ("Ottimo")
elif voto >= 60:
    print ("Buono")
elif voto >= 40:
    print("Malino")
elif voto >= 0:
    print("Malissimo")
else:
    print("Non puoi andare in negativo")


if voto < 0:
    print("No voti negativi")
elif voto >= 0 and voto < 40:
    print("Malissimo")
elif voto >= 40 and voto < 60:
    print("Malino")
elif voto >= 60 and voto < 80:
    print("Buono")
else:
    print("Ottimo")
    

# FESTA con invito ed età
etaCliente = 17
invito = False

if etaCliente >= 18 and invito:
    print("Benvenuto alla festa, puoi entrare")
elif etaCliente >= 18 and not invito:
    print("Non puoi entrare perché non hai un invito, anche se sei maggiorenne")
elif etaCliente < 18 and invito:
    print("NOn puoi entrare, non hai 18 anni anche se hai un invito")
else:
    print("Non puoi proprio entrare")
    
    
# Esempio if annidati - Patente
etaUser = 8
esameScritto = False

if etaUser >= 18:
    if esameScritto:
        print("Puoi sostenere l'esame pratico")
    else:
        print("Non puoi ancora sostenere l'esame pratico")
else:
    print("Mi spiace, non hai l'età per conseguire la patente")