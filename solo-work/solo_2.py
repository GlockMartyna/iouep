def trojkat (bok1, bok2, bok3, wys):
    pole = bok1*wys/2
    obw=bok1+bok2+bok3
    return pole, obw

print(f'Pole i obwod wynosza: {trojkat(10, 15, 12, 8)}')

def kwadrat (boka):
    polek=boka*boka
    obwk=4*boka
    return polek, obwk

print(f'Pole i obwod kwadratu wynosza: {kwadrat(6)}')

def prostokat(a,b):
    polep=a*b
    obwp=2*a+2*b
    return polep, obwp
print(f'Pole i obwod prostokata wynosza: {prostokat(6,5)}')
