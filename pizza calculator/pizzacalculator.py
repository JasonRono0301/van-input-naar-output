#Jason Ronoastro: pizza calculator

#Per afmeting van de pizza en met de prijzen erbij.
smallPizza = 1.50
mediumPizza = 2.00
largePizza = 2.50

#Output met de overzichten van de pizza en de prijzen erbij.
print(' |Small pizza price = 1.50 euro \n |Medium pizza price = 2.00 euro \n |Large pizza = 2.50 euro \n')

#Variabele voor de aantal bestelde pizza die de gebruiker gaat bestellen.
QTYsmall = int(input('|Aantal small pizza?: '))
QTYmedium = int(input('|Aantal medium pizza?: '))
QTYlarge = int(input('|Aantal large pizza?: '))

print('\n')

#Het overzicht van de bestelling die de gebruiker heeft gemaakt.
print('|Aantal bestelde small pizza: ' + str(QTYsmall) + '\n' + '|Aantal bestelde medium pizza: ' + str(QTYmedium) + '\n' + '|Aantal bestelde large pizza: ' + str(QTYlarge) + '\n')

total = float(QTYsmall*smallPizza + QTYmedium*mediumPizza + QTYlarge*largePizza)
print('Het totale bedrag = ' + str(total) + ' euro')
