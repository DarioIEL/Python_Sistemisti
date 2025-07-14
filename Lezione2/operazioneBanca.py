# Chiedi il nome all'utente
# Impostato un saldo di 1000 euro fai prima versare dei soldi e poi prelevare dei soldi. alla fine mostra il saldo a terminale

nomeUtente = input("Come ti chiami ?")
saldo = 1000
print("Benvenuto sul tuo conto in banca, il tuo saldo è di:", saldo)

versamento = float(input("Quanto vuoi versare?\n"))
saldo += versamento
print("Hai appena versato:", versamento, "\nIl tuo saldo attuale è di:","%.2f"%saldo)

prelievo = float(input("Quanto vuoi prelevare?\n"))
saldo -= prelievo
print("Hai appena prelevato:", prelievo, "\nIl tuo saldo attuale è di:","%.2f"%saldo)