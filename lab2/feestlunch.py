QTYcroissant = int(input('Aantal croissant: '))
QTYstokbrood = int(input('Aantal stokbrood: '))

priceCroissant = int(0.39) + 0.39 * QTYcroissant
priceStokbrood = int(2.78) / 10 * QTYstokbrood
Totalprice = priceCroissant + priceStokbrood
print(float(Totalprice))



