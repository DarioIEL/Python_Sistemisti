# Operatore di assegnazione = e tipi di dato primitivi
miaVarNum = 12; #Integer
miaVarString = "Ciao"
miaVarFloat = 32.2
miaVarBoole = True

# Operatori matematici aritmetici
somma = 5 + 6
diff = 8 - 3
molt = 9 * 5
div = 8 / 4.1
print("La somma vale", somma)

# Modulo (resto della divisione)
modulo = 8 % 2 # 0
print("Il modulo tra 8 e 2 vale", modulo)

# Potenza
potenza = 5 ** 3 # 125 --> 5 ^ 3 

# Divisione intera
divIntera = 5 // 3 # 1

# Operatori di assegnazione Composti
x = 10
x += 5 # Autoincremento x = x + 5 --> 15
x -= 3 # 12
x *= 2 # 24
x /= 4 # 6
x //= 2 # 3
x **= 3
x %= 2
print("la var x vale", x)

parola1 = "Ciao"
parola1 += " Mondo"
print(parola1)

# Operatori di confronto, tutti gli op di confronto producono un boolean
# a, b = 0,0
a = 9
b = 4

print(a == b) # False
print (a != b ) # True, != diverso; ! operatore NOT logico
print (a > b)
print (a < b)
print (a >= b)
print (a <= b)

# OPERATORI LOGICI and, or, not. Questi servono a mettere insieme più condizioni e valutarle 
print ("Operatrori logici")
print ("AND logico")
print (True and False) # False
print (True and True) # True
print (False and True) # False
print (False and False) # False

print ("OR logico")
print (True or False) # True
print (True or True) # True
print (False or True) # True
print (False or False) # False

# esempio età con invito alla festa. Per poter partecipare alla festa bisogna avere più di 18 anni e possedere un invito 
# CIT: io non volevo solo partecipare alla feste ma volevo avere il potere di farle fallire

eta = 20
invito = True
partecipazione = (eta >= 18) and (invito == True)

print ("Posso partecipare alla festa ?", partecipazione)

# Posso partecipare alla festa se sono maggiorenne oppure se sono stato invitato
eta2 = 14
invito2 = False

partecipazione2 = (eta2 >= 18) or (invito2)
print ("Posso partecipare alla festa ?", partecipazione2)

